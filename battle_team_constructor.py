import csv
import pandas as pd
import numpy as np

COVERAGE = 460
SAFETY = 333
COVERAGE_AVG = 700
OWN_POKEMON = 3

reader = pd.read_csv('battle.csv', header=None)
data = np.array(reader.values[1:, 1:]).astype(np.float64)

for i, battleRateRowI in enumerate(data[1:]):
    for j, battleRateRowJ in enumerate(data[1:]):
        if(i>=j):
            continue
        for k, battleRateRowK in enumerate(data[1:]):
            if(j>=k):
                continue

            teamCoverage = np.max(np.array([battleRateRowI, battleRateRowJ, battleRateRowK]), axis=0)[1:]
            teamSafety = (battleRateRowI[1:] + battleRateRowJ[1:] + battleRateRowK[1:])/3
            teamCounters = battleRateRowI[1:] + battleRateRowJ[1:] + battleRateRowK[1:]
            
            if (data[i+1][0] + data[j+1][0] + data[k+1][0] >= OWN_POKEMON) and (all(e >= COVERAGE for e in teamCoverage) and (all(e >= SAFETY for e in teamSafety) and (np.average(teamCoverage, weights=data[0][1:]) > COVERAGE_AVG))):
                print("1. {}\n2. {}\n3. {}\n".format(reader.values[i+2][0], reader.values[j+2][0], reader.values[k+2][0]))
                print("Coverage Avg: {}\nSafety Avg: {}\n".format(np.average(teamCoverage, weights=data[0][1:]), np.average(teamSafety, weights=data[0][1:])))
                print("Weakest: {} {}\nCounter: {} {}\n".format(reader.values[0][np.argmin(teamCoverage)+2], np.min(teamCoverage), reader.values[0][np.argmin(teamCounters)+2], np.min(teamCounters)/3))