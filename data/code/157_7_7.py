import numpy as np

def find_smallest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return np.amin(data)

if __name__ == '__main__':
    sample_list = [15, 3, -2, 7, 0, 8, -1]
    print(f"Smallest in {sample_list}: {find_smallest(sample_list)}")