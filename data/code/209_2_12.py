import numpy as np

def compute_average(values):
    return np.mean(values)

if __name__ == '__main__':
    sample_values = [150, 250, 350]
    average = compute_average(sample_values)
    print(average)