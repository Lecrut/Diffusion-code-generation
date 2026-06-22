import numpy as np

def apply_percentage_change(weights, change_rate):
    weights_array = np.asarray(weights)
    return (weights_array * (1.0 + change_rate)).tolist()

if __name__ == '__main__':
    sample_weights = [100.0, 200.5, 150.25, 75.0]
    rate = 0.10
    result = apply_percentage_change(sample_weights, rate)
    print(result)