import numpy as np

def apply_weight_change(weights, percentage_change):
    if percentage_change == 0:
        return weights
    factor = 1 + percentage_change
    return weights * factor

if __name__ == '__main__':
    sample_weights = np.array([10.0, 20.0, 30.0, 40.0, 50.0])
    change_percentage = 0.10
    result = apply_weight_change(sample_weights, change_percentage)
    print(result)