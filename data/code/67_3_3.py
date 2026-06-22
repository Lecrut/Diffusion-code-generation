import numpy as np

def convert_liters_to_milliliters(liters: np.ndarray) -> np.ndarray:
    return liters * 1000.0

if __name__ == '__main__':
    sample_values = np.array([0.5, 1.0, 2.5, 10.0, 0.001], dtype=np.float64)
    result = convert_liters_to_milliliters(sample_values)
    print(result)