import numpy as np

def compute_average(values):
    return np.mean(values)

if __name__ == '__main__':
    sample_values = [250, 350, 450]
    average = compute_average(sample_values)
    print(average)