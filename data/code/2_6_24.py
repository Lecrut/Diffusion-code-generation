import numpy as np

def calculate_volumes(volumes, scale_factor):
    return volumes * scale_factor

if __name__ == '__main__':
    sample_volumes = np.array([10.0, 20.0, 30.0, 40.0, 50.0])
    scale_factor = 1.5
    scaled_volumes = calculate_volumes(sample_volumes, scale_factor)
    print(scaled_volumes)