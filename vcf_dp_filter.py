#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#input with all genotypes
#cluster_1_size_1	0	SNP_higher_path_1000037	A	C	.	.	.	GT:DP:PL:AD:HQ	0/0:5:4,19,104:5,0:93,0	0/1:9:63,10,83:5,4:96,89	0/0:1:5,37,224:1,0:94,0	
#output with low covered as missing (<3 for example)
#cluster_1_size_1	0	SNP_higher_path_1000037	A	C	.	.	.	GT:DP:PL:AD:HQ	0/0:5:4,19,104:5,0:93,0	0/1:9:63,10,83:5,4:96,89	./.:1:5,37,224:1,0:94,0	

import sys
import csv

def import_file(path,out,val):
	with open(path,'r') as fd, open(out,'w') as outfile:
		for fields in csv.reader(fd, delimiter='\t'):
			if fields[0].startswith("#"):
				outfile.write('\t'.join(fields)+'\n')
			else:
				header = fields[0:9]
				outfile.write('\t'.join(header)+'\t')
				for field in fields[9:]:
					info = field.split(':')
					if int(info[1]) <= int(val):
						info[0] = './.'
					outfile.write(':'.join(info)+'\t')
				outfile.write('\n')

import_file(sys.argv[1],sys.argv[2],sys.argv[3])
