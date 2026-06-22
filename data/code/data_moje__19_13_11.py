import numpy as np

def get_random_element(arr: np.ndarray):
    if arr.size == 0:
        raise ValueError("Input array is empty")
    idx = np.random.randint(0, arr.size)
    return arr.flat[idx]

if __name__ == "__main__":
    large_array = np.arange(1000000)
    selected_value = get_random_element(large_array)
    print(selected_value)