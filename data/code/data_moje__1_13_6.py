import numpy as np

def apply_percentage_change(weights, percentage):
    weights_array = np.asarray(weights)
    return (weights_array * (1 + percentage)).tolist()

if __name__ == '__main__':
    sample_weights = [10.5, 20.3, 15.7, 30.1, 5.2]
    change_percentage = 0.15
    result = apply_percentage_change(sample_weights, change_percentage)
    print(result)