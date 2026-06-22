import numpy as np

def process_volume_measurements(volumes):
    arr = np.asarray(volumes, dtype=np.float64)
    if arr.ndim != 1:
        raise ValueError("Input must be a 1-dimensional array-like.")
    positive_mask = arr > 0
    positive_volumes = arr[positive_mask]
    if positive_volumes.size == 0:
        raise ValueError("No positive volume measurements provided.")
    log_volumes = np.log(positive_volumes)
    mean_log = np.mean(log_volumes)
    std_log = np.std(log_volumes)
    z_scores = (positive_volumes - np.exp(mean_log)) / std_log if std_log > 0 else np.zeros_like(positive_volumes)
    scaled_volumes = positive_volumes * 1.5
    return {
        "original_count": len(arr),
        "positive_count": positive_volumes.size,
        "min": np.min(arr),
        "max": np.max(arr),
        "mean_log_volume": mean_log,
        "std_log_volume": std_log,
        "z_scores": z_scores,
        "scaled_volumes": scaled_volumes
    }

if __name__ == '__main__':
    sample_volumes = [10.0, 20.0, 30.0, 5.0, 50.0]
    result = process_volume_measurements(sample_volumes)
    print(f"Original: {sample_volumes}")
    print(f"Mean Log Volume: {result['mean_log_volume']}")
    print(f"Std Log Volume: {result['std_log_volume']}")
    print(f"Scaled Volumes: {result['scaled_volumes']}")
    print(f"Z-Scores: {result['z_scores']}")