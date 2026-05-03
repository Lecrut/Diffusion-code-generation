import numpy as np
def volume_scaling_module():
    volumes = np.array([10.5, 22.1, 35.8, 41.0, 55.3])
    scaling_factors = np.array([1.5, 2.0, 1.1, 1.8, 1.3])
    scaled_volumes = volumes * scaling_factors
    return scaled_volumes
if __name__ == '__main__':
    result = volume_scaling_module()
    print(result)