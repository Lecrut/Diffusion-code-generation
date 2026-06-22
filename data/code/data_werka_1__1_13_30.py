import numpy as np

def apply_weight_change(weights, percentage_change):
    return weights * (1 + percentage_change)
if __name__ == '__main__':
    sample_weights = [70.5, 68.2, 80.3, 95.1]
    percentage_change = 0.05
    new_weights = apply_weight_change(np.array(sample_weights), percentage_change)
    print(new_weights.tolist())