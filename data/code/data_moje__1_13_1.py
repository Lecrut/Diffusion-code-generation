import numpy as np

def apply_weight_change(weights: list, change: float) -> list:
    weight_array = np.array(weights, dtype=float)
    new_weights = weight_array * (1 + change)
    return new_weights.tolist()

if __name__ == '__main__':
    sample_weights = [100.0, 200.0, 300.0]
    change_percentage = 0.10
    result = apply_weight_change(sample_weights, change_percentage)
    print(result)