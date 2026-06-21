import numpy as np
SAMPLE_VALUES = [100, 200, 300]

def compute_average(values):
    return np.mean(values)
if __name__ == '__main__':
    result = compute_average(SAMPLE_VALUES)
    print(result)