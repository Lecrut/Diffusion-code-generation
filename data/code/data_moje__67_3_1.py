import numpy as np

def convert_liters_to_milliliters(liters: np.ndarray) -> np.ndarray:
    return liters * 1000

if __name__ == '__main__':
    sample_liters = np.array([1.5, 2.0, 0.75, 3.14])
    result = convert_liters_to_milliliters(sample_liters)
    print(result)