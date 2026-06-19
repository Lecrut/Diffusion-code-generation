import numpy as np

def adjust_weights(weights, percentage_change):
    return weights * (1 + percentage_change)
if __name__ == '__main__':
    sample_weights = [70, 80, 90, 100]
    percentage_change = 0.05
    adjusted_weights = adjust_weights(np.array(sample_weights), percentage_change)
    print(adjusted_weights.tolist())