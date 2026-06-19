import numpy as np

def calculate_area_difference(area1, area2):
    diff = np.bitwise_xor(area1, area2)
    return np.sum(diff)

if __name__ == '__main__':
    matrix_a = np.array([
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]
    ])
    
    matrix_b = np.array([
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1]
    ])
    
    result1 = calculate_area_difference(matrix_a, matrix_b)
    print(result1)
    
    matrix_c = np.array([
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ])
    
    matrix_d = np.array([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ])
    
    result2 = calculate_area_difference(matrix_c, matrix_d)
    print(result2)
    
    matrix_e = np.array([
        [1, 0, 1],
        [0, 0, 0],
        [1, 0, 1]
    ])
    
    matrix_f = np.array([
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ])
    
    result3 = calculate_area_difference(matrix_e, matrix_f)
    print(result3)