import numpy as np

def scale_volumes(volumes, scaling_factor):
    volumes_array = np.asarray(volumes, dtype=float)
    return volumes_array * scaling_factor

def compute_normalized_volumes(volumes):
    volumes_array = np.asarray(volumes, dtype=float)
    min_val = volumes_array.min()
    max_val = volumes_array.max()
    if max_val == min_val:
        return np.zeros_like(volumes_array)
    return (volumes_array - min_val) / (max_val - min_val)

def compute_volume_statistics(volumes):
    volumes_array = np.asarray(volumes, dtype=float)
    return {
        'mean': np.mean(volumes_array),
        'std': np.std(volumes_array),
        'min': np.min(volumes_array),
        'max': np.max(volumes_array),
        'sum': np.sum(volumes_array)
    }

if __name__ == '__main__':
    sample_volumes = [1.5, 2.3, 4.7, 0.8, 3.1, 5.2, 1.9, 4.0, 2.5, 3.7]
    
    scaled = scale_volumes(sample_volumes, 2.5)
    print(scaled)
    
    normalized = compute_normalized_volumes(sample_volumes)
    print(normalized)
    
    stats = compute_volume_statistics(sample_volumes)
    print(stats)