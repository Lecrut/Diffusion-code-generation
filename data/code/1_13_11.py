import numpy as np

def apply_weight_change(weights, change_percent):
    np_weights = np.asarray(weights, dtype=np.float64)
    return (np_weights * (1 + change_percent)).tolist()

if __name__ == '__main__':
    sample_weights = [100, 200, 300, 400, 500]
    sample_change = 0.1
    result = apply_weight_change(sample_weights, sample_change)
    print(result)