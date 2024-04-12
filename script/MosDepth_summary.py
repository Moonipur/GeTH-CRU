#!/bin/python

import sys, os
import pandas as pd
import numpy as np

file_path = sys.argv[1]

chr = [
    "chr1", "chr2", "chr3", "chr4", "chr5", "chr6",
    "chr7", "chr8", "chr9", "chr10", "chr11", "chr12",
    "chr13", "chr14", "chr15", "chr16", "chr17", "chr18",
    "chr19", "chr20", "chr21", "chr22", "chrX", "chrY"
]

df = pd.read_table(file_path, sep='\t')

file_path_sp = list(os.path.split(file_path))
name = [*map(file_path_sp[-1].split('.').__getitem__,[0,3])]
name.insert(1, "FINE_SUMMARY")
file_path_sp[-1] = '.'.join(name)
out_file = os.path.join(*file_path_sp)

data = []
for i in chr:
  if df.loc[df['chrom'] == i].iloc[0,0] == i:
    data.append([i,df.loc[df['chrom'] == i].iloc[0,3]])

mean_coverage=np.mean([data[i][1] for i in range(len(data))])

new_df = pd.DataFrame(data, columns=["chrom", "mean_depth"])
new_df.loc[len(new_df.index)] = ["Coverage", np.round(mean_coverage, 2)]
new_df.to_csv(out_file, index=False, sep='\t')