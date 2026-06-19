import numpy as np

def compare_lengths(array1, array2):
    return np.sign(array1 - array2)

if __name__ == '__main__':
    lengths1 = np.array([10, 20, 30, 40])
    lengths2 = np.array([15, 20, 25, 35])
    
    result = compare_lengths(lengths1, lengths2)
    print(result)