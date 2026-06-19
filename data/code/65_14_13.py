import numpy as np

def extract_elements(array, indices):
    return array[indices]

if __name__ == '__main__':
    data_array = np.array([15, 25, 35, 45, 55, 65, 75])
    index_positions = np.array([1, 3, 5])
    extracted_values = extract_elements(data_array, index_positions)
    print(extracted_values)