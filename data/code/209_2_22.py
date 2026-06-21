import numpy as np

def calculate_average(values):
    return np.mean(values)

if __name__ == '__main__':
    sample_values = [400, 500, 600]
    result = calculate_average(sample_values)
    print(result)