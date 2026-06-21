import numpy as np

def compute_median(data):
    return np.median(data)

if __name__ == '__main__':
    sample_values = [
        [1, 5, 2, 8, 3],
        [10, 20, 30, 40, 50, 60],
        [7],
        []
    ]
    
    for values in sample_values:
        print(f"Median of {values} is: {compute_median(values)}")