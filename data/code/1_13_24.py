import numpy as np

def adjust_weights(weights, change_percentage):
    return weights * (1 + change_percentage)
if __name__ == '__main__':
    sample_weights = [70.5, 68.2, 85.3, 90.1]
    percentage_change = 0.05
    adjusted_weights = adjust_weights(np.array(sample_weights), percentage_change)
    print(adjusted_weights.tolist())