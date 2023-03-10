import numpy as np
import csv

turnoverMean = 47.08064516
turnoverSD = 14.98556506

# single family to two unit
for i in np.arange(0, 1, 0.01):
    # single family to three unit
    for j in np.arange(0, 1 - i, 0.01):
        # single family to four unit
        for k in np.arange(0, 1 - i - j, 0.01):
            twoUnitPercentage = round(i, 2)
            threeUnitPercentage = round(j, 2)
            fourUnitPercentage = round(k, 2)

            singleFamilyPercentage = 1 - twoUnitPercentage - threeUnitPercentage - fourUnitPercentage
            totalNewUnits = 0

            # run 10000 experiments
            for i in range(10000):
                newUnits = 0

                # simulate every month until 2040
                for month in range(204):
                    turnovers = np.random.normal(turnoverMean, turnoverSD, None)
                    rand = np.random.random()

                    if rand < singleFamilyPercentage: 
                        newUnits = newUnits
                    elif rand < singleFamilyPercentage + twoUnitPercentage:
                        newUnits += 1
                    elif rand < singleFamilyPercentage + twoUnitPercentage + threeUnitPercentage:
                        newUnits += 2
                    else:
                         newUnits += 3

                totalNewUnits += newUnits
            
            averageNewUnits = totalNewUnits / 10000

            # calculate number of new units short of job growth
            housingShortageCoefficient = round(16335 - averageNewUnits)

            # write to csv
            file = open("sunnyvaleResults.csv", "a")

            writer = csv.writer(file)
            writer.writerow([str(singleFamilyPercentage), str(twoUnitPercentage), str(threeUnitPercentage), str(fourUnitPercentage), str(housingShortageCoefficient)])

            file.close()