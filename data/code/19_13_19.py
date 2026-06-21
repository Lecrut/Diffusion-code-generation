import numpy as np

def get_random_element(arr):
    if arr.size == 0:
        raise ValueError("Cannot select from an empty array")
    idx = np.random.randint(0, arr.size)
    return arr.flat[idx]

if __name__ == '__main__':
    sample_data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    result = get_random_element(sample_data)
    print(result)