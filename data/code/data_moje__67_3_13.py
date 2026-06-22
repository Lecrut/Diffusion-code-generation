import numpy as np

def liters_to_milliliters(liters_array):
    return liters_array * 1000
if __name__ == '__main__':
    sample_liters = np.array([1.0, 2.5, 0.5, 3.75, 10.0])
    sample_milliliters = liters_to_milliliters(sample_liters)
    print(sample_milliliters)