import numpy as np

def apply_weight_change(weights, change):
    weights_array = np.asarray(weights, dtype=float)
    return weights_array * (1 + change)

if __name__ == '__main__':
    sample_weights = [50.5, 62.3, 75.0, 88.2, 91.4]
    change_factor = 0.1
    result = apply_weight_change(sample_weights, change_factor)
    print(result.tolist())