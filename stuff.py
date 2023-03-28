import numpy as np
import pandas as pd

x = pd.DataFrame(np.zeros((10,10)))
print(x,"\n")
x.iloc[:] = 150
print(x,"\n")
