import numpy as np

def liters_to_milliliters(liters):
    liters_array = np.asarray(liters)
    return liters_array * 1000.0

if __name__ == '__main__':
    sample_liters = np.array([0.5, 1.25, 3.0, 10.75, 0.001])
    result = liters_to_milliliters(sample_liters)
    print(result)