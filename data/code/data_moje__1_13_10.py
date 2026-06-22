import numpy as np

def apply_percentage_change(weights, percentage_change):
    weights_array = np.array(weights)
    return (weights_array * (1 + percentage_change)).tolist()

if __name__ == '__main__':
    sample_weights = [100.5, 200.0, 50.25, 75.5]
    change_percentage = 0.1
    result = apply_percentage_change(sample_weights, change_percentage)
    print(result)