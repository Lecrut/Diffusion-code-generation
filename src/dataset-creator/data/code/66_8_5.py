import numpy as np
def process_weights(weights):
    weights_array = np.array(weights)
    differences = np.diff(weights_array)
    return list(differences)
if __name__ == '__main__':
    sample_data = [10, 25, 30, 45, 60]
    result = process_weights(sample_data)
    print(result)