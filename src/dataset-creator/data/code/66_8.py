import numpy as np
def process_weights(weights):
    weights = np.array(weights)
    differences = np.diff(weights)
    return differences
if __name__ == '__main__':
    sample_data = [10, 25, 30, 45, 60]
    result = process_weights(sample_data)
    print(result.tolist())