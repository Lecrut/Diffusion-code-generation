import numpy as np

def calculate_volumes(volumes):
    return volumes * 2.0

if __name__ == '__main__':
    sample_volumes = np.array([10, 20, 30, 40, 50])
    result = calculate_volumes(sample_volumes)
    print(result)