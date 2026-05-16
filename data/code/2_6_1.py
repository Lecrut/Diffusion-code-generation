import numpy as np
def volume_scaling_module():
    volumes = np.array([10.5, 22.1, 5.8, 30.0, 15.3])
    scaling_factors = np.array([2.5, 1.8, 3.0, 1.5, 2.2])
    scaled_volumes = volumes * scaling_factors
    return scaled_volumes
if __name__ == '__main__':
    result = volume_scaling_module()
    print(result)