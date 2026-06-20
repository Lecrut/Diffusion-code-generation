import numpy as np

def apply_percentage_change(measurements, change_percentage):
    weights_array = np.array(measurements, dtype=float)
    return (weights_array * (1.0 + change_percentage)).tolist()

if __name__ == '__main__':
    sample_weights = [100.5, 200.0, 150.75, 300.25, 50.0]
    percentage_change = 0.15
    result = apply_percentage_change(sample_weights, percentage_change)
    print(result)