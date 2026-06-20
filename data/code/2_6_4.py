import numpy as np

def scale_volume_measurements(volumes, factor):
    return volumes * factor

def compute_volume_statistics(volumes):
    mean_volume = np.mean(volumes)
    std_volume = np.std(volumes)
    min_volume = np.min(volumes)
    max_volume = np.max(volumes)
    return mean_volume, std_volume, min_volume, max_volume

if __name__ == '__main__':
    volume_data = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    scaling_factor = 2.5

    scaled_volumes = scale_volume_measurements(volume_data, scaling_factor)
    mean, std, min_val, max_val = compute_volume_statistics(volume_data)

    print(scaled_volumes)
    print(mean, std, min_val, max_val)