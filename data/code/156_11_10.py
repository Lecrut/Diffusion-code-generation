import numpy as np

def compute_mean():
    data = np.array([10, 20, 30, 40, 50])
    mean_value = np.mean(data)
    return mean_value

if __name__ == '__main__':
    result = compute_mean()
    print(result)