import numpy as np

def compute_volume_statistics(volumes):
    volumes_array = np.asarray(volumes, dtype=float)
    total_volume = np.sum(volumes_array)
    mean_volume = np.mean(volumes_array)
    std_volume = np.std(volumes_array)
    scaled_volumes = volumes_array * 2.0
    return {
        'total': total_volume,
        'mean': mean_volume,
        'std': std_volume,
        'scaled': scaled_volumes
    }

if __name__ == '__main__':
    sample_volumes = [1.5, 2.3, 4.7, 3.2, 5.1, 0.9, 6.4, 3.8]
    result = compute_volume_statistics(sample_volumes)
    print(result)