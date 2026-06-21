import numpy as np

def apply_percentage_change(weights, percentage_change):
    weights_array = np.array(weights)
    adjusted_weights = weights_array * (1 + percentage_change)
    return adjusted_weights.tolist()
if __name__ == '__main__':
    sample_weights = [70, 80, 90, 100]
    percentage_change = 0.1
    new_weights = apply_percentage_change(sample_weights, percentage_change)
    print(new_weights)