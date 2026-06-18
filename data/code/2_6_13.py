import numpy as np

def calculate_volume_stats(volume_measurements):
    """
    Performs vectorized calculations on an array of volume measurements.
    
    This function demonstrates high-performance scaling operations using NumPy's
    built-in optimized functions instead of Python loops. It calculates the total 
    volume, mean volume, standard deviation, and variance for the input data.

    Parameters:
        volume_measurements (np.ndarray): An array-like object containing volume measurements.

    Returns:
        dict: A dictionary containing the results of the calculations with keys:
            - 'total_volume': sum of all volumes
            - 'mean_volume': average volume
            - 'std_deviation': standard deviation of volumes
            - 'variance': variance of volumes
    """
    # Convert input to numpy array for vectorized operations if not already an array instance
    data = np.asarray(volume_measurements)

    total_volume = np.sum(data)
    mean_volume = np.mean(data)
    std_deviation = np.std(data, ddof=0)  # Population standard deviation
    variance = np.var(data, ddof=0)       # Population variance (consistent with std calculation)

    return {
        'total_volume': total_volume,
        'mean_volume': mean_volume,
        'std_deviation': std_deviation,
        'variance': variance
    }

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files needed)
    sample_volumes = np.array([10.5, 23.7, 45.2, 89.1, 67.3, 12.9, 34.5])

    print("Input Volume Measurements:", sample_volumes)
    
    # Perform vectorized calculations
    results = calculate_volume_stats(sample_volumes)
    
    print("\nCalculated Statistics:")
    print(f"Total Volume: {results['total_volume']:.2f}")
    print(f"Mean Volume:   {results['mean_volume']:.2f}")
    print(f"Std Deviation: {results['std_deviation']:.2f}")
    print(f"Variance:      {results['variance']:.2f}")

    # Demonstration with a larger array to show scaling capability
    large_sample = np.random.randint(1, 1000, size=5000)
    print("\nDemonstrating performance on scaled dataset (5000 items):")
    
    start_time = __import__('time').perf_counter()
    results_large = calculate_volume_stats(large_sample)
    end_time = __import__('time').perf_counter()

    execution_time = end_time - start_time
    
    print(f"Total Volume: {results_large['total_volume']:.2f}")
    print(f"Execution Time for 5000 items: {execution_time*1e6:.4f} µs")