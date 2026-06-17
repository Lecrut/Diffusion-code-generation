import numpy as np
def process_weights(weights):
    return np.diff(np.array(weights), axis=0)
if __name__ == '__main__':
    sample_data = [10, 25.5, 30.2, 45.8, 60]
    result = process_weights(sample_data)
    print(result)