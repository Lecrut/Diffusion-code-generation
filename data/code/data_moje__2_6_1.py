import numpy as np

def scale_volumes(volumes, scale_factors):
    return volumes * scale_factors

def calculate_volume_statistics(volumes, scale_factors):
    scaled_volumes = scale_volumes(volumes, scale_factors)
    return {'mean': np.mean(scaled_volumes), 'median': np.median(scaled_volumes), 'std': np.std(scaled_volumes)}
if __name__ == '__main__':
    volumes = np.array([10.0, 20.0, 30.0, 40.0, 50.0])
    scale_factors = np.array([2.0, 1.5, 3.0, 0.5, 2.5])
    scaled_volumes = scale_volumes(volumes, scale_factors)
    print(scaled_volumes)
    stats = calculate_volume_statistics(volumes, scale_factors)
    print(stats)