import numpy as np
def process_weight_data(weights: list) -> tuple:
    weights_array = np.array(weights)
    differences = np.diff(weights_array)
    return weights_array, differences
if __name__ == '__main__':
    sample_weights = [10.5, 23.7, 45.2, 67.8, 90.1]
    processed_data = process_weight_data(sample_weights)
    print(processed_data[0])
    print(processed_data[1])