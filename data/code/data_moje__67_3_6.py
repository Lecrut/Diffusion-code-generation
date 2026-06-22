import numpy as np

def convert_liters_to_milliliters(liters: np.ndarray) -> np.ndarray:
    return liters * 1000.0

if __name__ == '__main__':
    liters_array = np.array([1.5, 0.25, 3.0, 0.75])
    result = convert_liters_to_milliliters(liters_array)
    print(result)