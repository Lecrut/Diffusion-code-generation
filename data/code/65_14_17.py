import numpy as np

def extract_elements(array, indices):
    return array[indices]

if __name__ == '__main__':
    data_array = np.array([100, 200, 300, 400, 500])
    selected_indices = np.array([1, 3])
    extracted_values = extract_elements(data_array, selected_indices)
    print(extracted_values)