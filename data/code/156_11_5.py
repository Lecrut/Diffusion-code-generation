import numpy as np

def compute_mean():
    data = np.array([10, 20, 30, 40, 50])
    return np.mean(data)

if __name__ == '__main__':
    print(compute_mean())