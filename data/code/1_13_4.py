import numpy as np

def adjust_weights(weights, change_percentage):
    weights_array = np.array(weights)
    return (weights_array * (1 + change_percentage)).tolist()

if __name__ == '__main__':
    sample_weights = [10.5, 20.3, 15.7, 30.1]
    sample_change = 0.1
    result = adjust_weights(sample_weights, sample_change)
    print(result)