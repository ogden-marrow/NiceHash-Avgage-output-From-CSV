import numpy as np
import pandas as pd

fileName = "mining_stats-2021-03-29.csv"

dat = pd.read_csv(fileName)

dat = dat.to_numpy()
dat = dat[3:]

print(dat[0])