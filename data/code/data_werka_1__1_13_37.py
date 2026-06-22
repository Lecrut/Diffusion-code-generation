import numpy as np

def adjust_weights(weights, change_percentage):
    weights_array = np.array(weights)
    adjusted_weights = weights_array * (1 + change_percentage)
    return adjusted_weights.tolist()
if __name__ == '__main__':
    sample_weights = [70.5, 68.2, 90.3, 85.7]
    percentage_change = 0.05
    new_weights = adjust_weights(sample_weights, percentage_change)
    print(new_weights)