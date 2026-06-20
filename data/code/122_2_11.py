import numpy as np

def average_of_floats(float_array):
    return np.mean(float_array)

if __name__ == '__main__':
    sample_values = np.array([1.5, 2.5, 3.5, 4.5, 5.5])
    print(average_of_floats(sample_values))