import numpy as np

def adjust_weights(weights, percentage_change):
    weights_array = np.array(weights)
    adjusted_weights = weights_array * (1 + percentage_change)
    return adjusted_weights.tolist()
if __name__ == '__main__':
    sample_weights = [70.5, 68.2, 75.3, 80.4, 69.8]
    percentage_change = 0.05
    new_weights = adjust_weights(sample_weights, percentage_change)
    print(new_weights)