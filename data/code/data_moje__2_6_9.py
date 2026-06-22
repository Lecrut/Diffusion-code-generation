import numpy as np

def scale_volumes(volumes, factor):
    return volumes * factor

def calculate_statistics(volumes):
    if volumes.size == 0:
        return {
            'mean': 0.0,
            'std': 0.0,
            'min': 0.0,
            'max': 0.0
        }
    return {
        'mean': np.mean(volumes),
        'std': np.std(volumes),
        'min': np.min(volumes),
        'max': np.max(volumes)
    }

def apply_threshold(volumes, threshold):
    return volumes[volumes > threshold]

def normalize_volumes(volumes):
    min_val = np.min(volumes)
    max_val = np.max(volumes)
    if max_val == min_val:
        return np.zeros_like(volumes)
    return (volumes - min_val) / (max_val - min_val)

def process_volumes(volumes, scale_factor, threshold):
    scaled = scale_volumes(volumes, scale_factor)
    stats = calculate_statistics(scaled)
    filtered = apply_threshold(scaled, threshold)
    normalized = normalize_volumes(scaled)
    return {
        'scaled': scaled,
        'statistics': stats,
        'filtered_count': filtered.shape[0],
        'normalized': normalized
    }

if __name__ == '__main__':
    volumes_data = np.array([10.5, 20.0, 30.5, 40.0, 50.5, 60.0, 70.5, 80.0, 90.5, 100.0])
    result = process_volumes(volumes_data, 2.0, 50.0)
    print(result['scaled'])
    print(result['statistics'])
    print(result['filtered_count'])
    print(result['normalized'])