import numpy as np

def find_maximum(data):
    if not isinstance(data, np.ndarray) or data.size == 0:
        raise ValueError("Input must be a non-empty NumPy array")
    return np.max(data)

if __name__ == '__main__':
    sample_data1 = np.array([10, 5, 20, 8])
    sample_data2 = np.array([3, 99, 1, 42])
    print(f"Maximum of {sample_data1}: {find_maximum(sample_data1)}")
    print(f"Maximum of {sample_data2}: {find_maximum(sample_data2)}")