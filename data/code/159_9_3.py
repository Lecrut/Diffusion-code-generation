import numpy as np

def extract_odd_elements(array):
    return array[array % 2 != 0]
if __name__ == '__main__':
    sample_array = np.array([11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    odd_elements = extract_odd_elements(sample_array)
    print(odd_elements)