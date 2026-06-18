import numpy as np

def calculate_volume_efficiency(volumes: np.ndarray) -> tuple[float, float]:
    """
    Performs vectorized calculations on an array of volume measurements.
    
    Calculates two key metrics efficiently using NumPy's broadcasting and built-in 
    functions to demonstrate high performance for scaling operations:
    1. Total Volume Sum (scalar)
    2. Coefficient of Variation (CV), a standardized measure of dispersion,
       calculated as std_dev / mean * 100% to express variability relative to the mean.

    Args:
        volumes (np.ndarray): Input array containing volume measurements.

    Returns:
        tuple[float, float]: A tuple containing (total_volume, cv_percentage).
    
    Note: This function assumes input is a valid numeric numpy array with at least 
    one element greater than zero to avoid division by zero in CV calculation.
    """
    total = np.sum(volumes)
    mean_val = np.mean(volumes)

    if mean_val == 0:
        cv = float('inf')
    else:
        std_dev = np.std(volumes, ddof=0)
        cv = (std_dev / mean_val) * 100.0
    
    return total, cv

if __name__ == '__main__':
    # Hard-coded sample volume measurements for demonstration purposes.
    # Represents liters of fluid in multiple containers or batches.
    sample_volumes = np.array([10.5, 23.7, 45.2, 89.1, 67.3], dtype=float)

    total_vol, cv_val = calculate_volume_efficiency(sample_volumes)

    print(f"Total Volume: {total_vol:.2f} liters")
    print(f"Coefficient of Variation (CV): {cv_val:.4f}%")