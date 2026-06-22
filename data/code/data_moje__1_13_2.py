import numpy as np

def apply_weight_change(weights, percentage_change):
    weights_array = np.array(weights, dtype=float)
    return (weights_array * (1.0 + percentage_change)).tolist()

if __name__ == '__main__':
    sample_weights = [100.5, 200.0, 150.25, 75.0]
    change_percent = 0.15
    result = apply_weight_change(sample_weights, change_percent)
    print(result)