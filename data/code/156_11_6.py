import numpy as np

def compute_mean(values):
    return np.mean(values)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    print(compute_mean(sample_values))