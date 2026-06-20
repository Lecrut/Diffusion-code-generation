import numpy as np

def adjust_weights(weights, percentage_change):
    arr = np.asarray(weights, dtype=float)
    return (arr * (1 + percentage_change)).tolist()

if __name__ == '__main__':
    sample_weights = [70.5, 65.2, 80.1, 92.4, 55.8]
    change_pct = 0.10
    result = adjust_weights(sample_weights, change_pct)
    print(result)