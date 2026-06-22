import numpy as np

def apply_percentage_change(weights, percentage_change):
    weight_array = np.asarray(weights, dtype=float)
    return (weight_array * (1 + percentage_change)).tolist()
if __name__ == '__main__':
    sample_weights = [100, 200, 300, 400, 500]
    change = 0.1
    result = apply_percentage_change(sample_weights, change)
    print(result)