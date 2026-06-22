import numpy as np

def liters_to_milliliters(liters):
    return np.asarray(liters, dtype=np.float64) * 1000.0

if __name__ == '__main__':
    sample_liters = np.array([0.5, 1.0, 2.5, 0.001, 1000.0])
    result = liters_to_milliliters(sample_liters)
    print(result)