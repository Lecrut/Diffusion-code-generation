import numpy as np

def filter_even_with_numpy():
    arr = np.arange(1, 21)
    even_mask = (arr % 2 == 0)
    return arr[even_mask]

if __name__ == '__main__':
    sample_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    result = filter_even_with_numpy()
    print(result)