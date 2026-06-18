import numpy as np

def calculate_volume_metrics(volumes):
    """
    Perform vectorized calculations on an array of volume measurements.
    
    This function demonstrates high-performance operations using NumPy's 
    vectorization capabilities to compute mean, standard deviation, and 
    total sum without explicit Python loops over individual elements.

    Parameters:
        volumes (np.ndarray): Input array of volume measurements.

    Returns:
        dict: A dictionary containing the computed metrics ('mean', 'std_dev', 'total').
    """
    # Ensure input is a NumPy array for optimal performance and safety
    if not isinstance(volumes, np.ndarray):
        volumes = np.array(volumes)
    
    mean_vol = np.mean(volumes)
    std_vol = np.std(volumes)
    total_vol = np.sum(volumes)

    return {
        'mean': float(mean_vol),
        'std_dev': float(std_vol),
        'total': int(total_vol) if volumes.dtype.kind == 'i' else float(total_vol)
    }

if __name__ == '__main__':
    # Hard-coded sample values representing volume measurements in cubic meters
    sample_volumes = np.array([10.5, 23.4, 17.8, 9.2, 31.6], dtype=float)

    print("Input Volume Measurements:", sample_volumes)
    
    metrics = calculate_volume_metrics(sample_volumes)
    
    print("\nComputed Metrics:")
    print(f"Mean Volume: {metrics['mean']}")
    print(f"Standard Deviation: {metrics['std_dev']:.2f}")
    print(f"Total Volume: {metrics['total']}")