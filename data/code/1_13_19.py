import numpy as np

def apply_percentage_change(weights, percentage_change):
    weights_array = np.array(weights, dtype=float)
    return (weights_array * (1.0 + percentage_change)).tolist()

if __name__ == '__main__':
    sample_weights = [10.0, 20.5, 30.25, 40.0]
    change_percentage = 0.1
    result = apply_percentage_change(sample_weights, change_percentage)
    print(result)