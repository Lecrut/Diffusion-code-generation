import numpy as np

def find_max_in_array(arr):
    return np.max(arr)

if __name__ == '__main__':
    sample_data = np.array([10, 5, 20, 8])
    print(f"Maximum of {sample_data}: {find_max_in_array(sample_data)}")