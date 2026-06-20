import numpy as np

def adjust_weights(weights, percentage_change):
    weights_array = np.array(weights, dtype=np.float64)
    adjusted = weights_array * (1.0 + percentage_change)
    return adjusted.tolist()

if __name__ == '__main__':
    sample_weights = [70.5, 65.2, 80.0, 92.1, 55.8]
    change_rate = 0.05
    result = adjust_weights(sample_weights, change_rate)
    print(result)