import numpy as np

def apply_weight_change(weights, percentage_change):
    weight_array = np.asarray(weights, dtype=np.float64)
    new_weights = weight_array * (1 + percentage_change)
    return new_weights.tolist()

if __name__ == '__main__':
    sample_weights = [10.0, 20.0, 30.0, 40.0, 50.0]
    change_percent = 0.1
    result = apply_weight_change(sample_weights, change_percent)
    print(result)