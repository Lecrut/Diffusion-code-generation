import numpy as np

def apply_weight_change(weights, change_percentage):
    weight_array = np.array(weights, dtype=np.float64)
    return weight_array * (1 + change_percentage).tolist()

if __name__ == '__main__':
    sample_weights = [100.0, 200.0, 300.0]
    sample_change = 0.1
    result = apply_weight_change(sample_weights, sample_change)
    print(result)