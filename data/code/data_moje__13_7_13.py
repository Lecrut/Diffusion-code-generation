import numpy as np

def extract_value(array: np.ndarray, index: tuple) -> float:
    return array[index]

if __name__ == '__main__':
    sample_array = np.arange(24).reshape(2, 3, 4)
    sample_index = (1, 2, 3)
    result = extract_value(sample_array, sample_index)
    print(result)