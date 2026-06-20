import numpy as np

def apply_weight_change(weights, change_percentage):
    weights_array = np.asarray(weights, dtype=float)
    return (weights_array * (1 + change_percentage)).tolist()

if __name__ == '__main__':
    sample_weights = [50.5, 60.0, 75.25, 80.0, 95.5]
    percentage_change = 0.10
    result = apply_weight_change(sample_weights, percentage_change)
    print(result)