import numpy as np

def apply_percentage_change(weights, percentage_change):
    weights_array = np.asarray(weights, dtype=float)
    return (weights_array * (1 + percentage_change)).tolist()

if __name__ == '__main__':
    sample_weights = [100.0, 200.5, 150.25, 300.0]
    change_factor = 0.1
    new_weights = apply_percentage_change(sample_weights, change_factor)
    print(new_weights)