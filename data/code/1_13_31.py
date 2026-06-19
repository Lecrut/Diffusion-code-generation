import numpy as np

def apply_weight_change(weights, change_percentage):
    return weights * (1 + change_percentage)
if __name__ == '__main__':
    sample_weights = [70.5, 68.2, 85.3, 90.1, 72.4]
    percentage_change = 0.05
    new_weights = apply_weight_change(np.array(sample_weights), percentage_change)
    print(new_weights.tolist())