import numpy as np

def scale_volumes(volumes, scale_factor):
    return np.multiply(volumes, scale_factor)

def convert_volumes_to_cubic_meters(volumes_cubic_cm):
    conversion_factor = 1e-6
    return np.multiply(volumes_cubic_cm, conversion_factor)

def compute_total_volume(volumes):
    return np.sum(volumes)

def compute_mean_volume(volumes):
    return np.mean(volumes)

if __name__ == '__main__':
    volume_data = np.array([100.5, 250.75, 300.0, 150.25, 500.0, 125.5])

    scaled_volumes = scale_volumes(volume_data, 2.5)
    print("Scaled Volumes:", scaled_volumes)

    converted_volumes = convert_volumes_to_cubic_meters(volume_data)
    print("Volumes in Cubic Meters:", converted_volumes)

    total_volume = compute_total_volume(volume_data)
    print("Total Volume:", total_volume)

    mean_volume = compute_mean_volume(volume_data)
    print("Mean Volume:", mean_volume)