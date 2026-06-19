import numpy as np

def apply_percentage_change(weights, percentage_change):
    return weights * (1 + percentage_change)
if __name__ == '__main__':
    sample_weights = [70.5, 68.2, 75.3, 69.8, 72.4]
    percentage_change = 0.05
    new_weights = apply_percentage_change(np.array(sample_weights), percentage_change)
    print(new_weights.tolist())