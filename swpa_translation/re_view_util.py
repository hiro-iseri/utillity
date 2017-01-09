#!/usr/bin/python
#coding: utf-8
'''
SWPA翻訳向け
原文にて、word.csvに含まれる単語があった場合、単語を@<w>{〜}で囲む
またnames.csvに含まれる単語があった場合、単語を@<n>{〜}で囲む
結果は標準出力に出力
実行例：python 本スクリプトファイルパス 原文ファイルパス word.csvファイルパス names.csvファイルパス >出力先
'''
import re
import sys
import csv

def get_word_list(data_file_path):
	word_list = [] 
	with open(data_file_path, 'r') as data_file:
		reader = csv.reader(data_file)
		for row in reader:
			word_list.append(row[0])
	word_list.sort(key = len, reverse = True) #単語数が多い用語を優先置換
	return word_list 
	
def run_re_view_util(input_file_path, data_file_path, name_file_path):
	word_list = get_word_list(data_file_path)
	name_list = get_word_list(name_file_path)
	with open(input_file_path, 'r') as read_file:
	    for line in read_file:
		for word in word_list:
			line = re.sub(r'(^|[\s\.\,\(\)])'+ word + r'($|[\s\.\,\(\)])', r'\1@<w>{' + word + r'}\2', line, re.M|re.I)
		for name in name_list:
			line = re.sub(r'(^|[\s\.\,\(\)])'+ word + r'($|[\s\.\,\(\)])', r'\1@<n>{' + word + r'}\2', line, re.M|re.I)
		sys.stdout.write(line)

if __name__ == "__main__":
	if len(sys.argv) != 4:
		print("argument error. specify \"re_view_util.py InputFilePath WordFilePath NameFilePath\".")
		sys.exit(0)
	run_re_view_util(sys.argv[1], sys.argv[2], sys.argv[3])
