import numpy as np

def process_volumes(volumes, scale_factor):
    scaled = volumes * scale_factor
    mean = np.mean(scaled)
    std = np.std(scaled)
    return {
        "original_min": np.min(volumes),
        "original_max": np.max(volumes),
        "scaled_mean": mean,
        "scaled_std": std,
        "total_volume": np.sum(scaled)
    }

if __name__ == '__main__':
    volumes = np.array([1.5, 2.0, 3.5, 4.0, 5.5])
    scale_factor = 2.0
    result = process_volumes(volumes, scale_factor)
    for key in result:
        print(f"{key}: {result[key]}")