import numpy as np

def calculate_volume_metrics(volumes):
    """
    Perform vectorized calculations on an array of volume measurements.
    
    This module demonstrates high-performance scaling operations using NumPy's 
    vectorization capabilities to avoid explicit Python loops over individual elements.
    
    Parameters:
        volumes (np.ndarray or list): Array of numerical volume values.
        
    Returns:
        dict: A dictionary containing key performance metrics derived from the input array,
              including total volume, mean volume, standard deviation, and count of outliers 
              defined as values greater than 1.5 times the median.
    
    Example usage (internal):
        volumes = [10, 20, 30, 40]
        metrics = calculate_volume_metrics(volumes)
        # Output: {'total': ..., 'mean': ..., ...}
    """
    
    if not isinstance(volumes, np.ndarray):
        volumes_array = np.array(volumes)
    else:
        volumes_array = volumes.copy()

    total_volume = np.sum(volumes_array)
    mean_volume = np.mean(volumes_array)
    std_volume = np.std(volumes_array)
    
    median_value = np.median(volumes_array)
    upper_threshold = 1.5 * median_value
    
    outliers_count = np.sum(np.array([v > upper_threshold for v in volumes_array]))

    return {
        "total": total_volume,
        "mean": mean_volume,
        "standard_deviation": std_volume,
        "median": median_value,
        "outlier_count": outliers_count
    }

if __name__ == '__main__':
    # Hard-coded sample volume measurements for demonstration purposes.
    # These values are static and do not require any user input or external files.
    sample_volumes = [100, 250, 375, 480, 610]

    print("Processing vectorized calculations on the following volume measurements:")
    for vol in sample_volumes:
        print(f"{vol}")

    # Compute and display results using NumPy's efficient operations.
    metrics = calculate_volume_metrics(sample_volumes)

    print("\nCalculated Metrics:")
    print("-" * 30)
    print(f"Total Volume: {metrics['total']}")
    print(f"Mean Volume:   {metrics['mean']:.2f}")
    print(f"Std Deviation: {metrics['standard_deviation']:.2f}")
    print(f"Median Value:  {metrics['median']:.2f}")
    print(f"Outlier Count: {metrics['outlier_count']}")

    # Verify that the calculation is vectorized by checking if inputs were converted to NumPy arrays internally.
    assert isinstance(metrics["total"], (int, float)), "Total volume should be a numeric type."
    assert metrics["mean"] == sum(sample_volumes) / len(sample_volumes), "Mean calculation verification failed."
    
    print("\nAll vectorized calculations completed successfully.")