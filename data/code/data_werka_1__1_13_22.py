import numpy as np

def apply_percentage_change(weights, percentage):
    return weights * (1 + percentage)
if __name__ == '__main__':
    sample_weights = [70, 80, 90, 100]
    percentage_change = 0.05
    new_weights = apply_percentage_change(np.array(sample_weights), percentage_change)
    print(new_weights.tolist())