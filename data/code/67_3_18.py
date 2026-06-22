import numpy as np

def convert_liters_to_milliliters(liters):
    return np.asarray(liters, dtype=np.float64) * 1000.0

if __name__ == '__main__':
    sample_values = np.array([0.5, 1.0, 2.5, 10.0, 100.0], dtype=np.float64)
    results = convert_liters_to_milliliters(sample_values)
    print(results)