import numpy as np

def extract_elements(array, indices):
    return array[indices]
if __name__ == '__main__':
    sample_array = np.array([10, 20, 30, 40, 50])
    indices_to_extract = [0, 2, 4]
    extracted_elements = extract_elements(sample_array, indices_to_extract)
    print(extracted_elements)