import numpy as np

def compute_average(values):
    return np.mean(values)

if __name__ == '__main__':
    sample_values = [100, 200, 300]
    average = compute_average(sample_values)
    print(average)