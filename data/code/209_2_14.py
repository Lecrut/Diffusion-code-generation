import numpy as np
SAMPLE_COUNT = 3

def calculate_average(values):
    return np.mean(values)
if __name__ == '__main__':
    sample_values = [100, 200, 300]
    average = calculate_average(sample_values)
    print(average)