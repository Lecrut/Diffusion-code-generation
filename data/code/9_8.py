import numpy as np
if __name__ == '__main__':
    measurements = np.array([10.0, 20.0, 30.0, 40.0, 50.0])
    volume_conversion_factor = 0.5
    volumes = measurements * volume_conversion_factor
    print(volumes)