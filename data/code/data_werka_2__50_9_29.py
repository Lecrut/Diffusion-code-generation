import numpy as np

def calculate_area_difference(region1, region2):
    if not isinstance(region1, np.ndarray) or not isinstance(region2, np.ndarray):
        raise ValueError('Both regions must be numpy arrays.')
    if region1.shape != region2.shape:
        raise ValueError('Both regions must have the same shape.')
    xor_result = np.bitwise_xor(region1, region2)
    area_diff = np.sum(xor_result)
    return area_diff

if __name__ == '__main__':
    sample_region1 = np.array([[1, 0, 1], [1, 1, 0], [0, 1, 1]])
    sample_region2 = np.array([[0, 1, 0], [1, 0, 1], [1, 1, 0]])
    
    area_diff_result = calculate_area_difference(sample_region1, sample_region2)
    print(area_diff_result)