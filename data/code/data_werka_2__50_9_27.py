import numpy as np

def validate_binary_matrix(matrix):
    if not isinstance(matrix, (np.ndarray, list)):
        raise ValueError('Input must be a numpy array or a list.')
    matrix = np.array(matrix)
    if not np.issubdtype(matrix.dtype, np.number) and not np.issubdtype(matrix.dtype, np.bool_):
        raise ValueError('Matrix elements must be either numbers or booleans.')
    if not np.all(np.logical_or(matrix == 0, matrix == 1)):
        raise ValueError('Matrix must contain only binary values (0 or 1).')
    return matrix

def area_difference(region1, region2):
    region1 = validate_binary_matrix(region1)
    region2 = validate_binary_matrix(region2)
    if region1.shape != region2.shape:
        raise ValueError('Both regions must have the same shape.')
    
    xor_result = np.bitwise_xor(region1, region2)
    area_diff = np.sum(xor_result)
    return area_diff

if __name__ == '__main__':
    region1 = [[1, 0, 1], [1, 1, 0], [0, 1, 1]]
    region2 = [[0, 1, 0], [1, 0, 1], [1, 1, 0]]
    difference = area_difference(region1, region2)
    print(difference)