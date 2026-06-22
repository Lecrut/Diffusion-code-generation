import numpy as np

def convert_to_milliliters(liters_array):
    return liters_array * 1000.0

if __name__ == '__main__':
    liters = np.array([1.5, 2.0, 3.75])
    result = convert_to_milliliters(liters)
    print(result)