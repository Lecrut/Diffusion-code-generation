import numpy as np

def calculate_volume_metrics(volumes: np.ndarray) -> dict[str, float]:
    """
    Performs vectorized calculations on an array of volume measurements.
    
    Parameters:
        volumes (np.ndarray): Input array containing volume values.
        
    Returns:
        dict: A dictionary containing the following metrics:
            - 'total_volume': Sum of all volumes.
            - 'mean_volume': Arithmetic mean of the volumes.
            - 'std_deviation': Standard deviation of the volumes.
            - 'min_volume': Minimum volume value.
            - 'max_volume': Maximum volume value.
    """
    # Ensure input is a NumPy array for vectorized operations
    arr = np.asarray(volumes)
    
    total_volume = np.sum(arr)
    mean_volume = np.mean(arr)
    std_deviation = np.std(arr, ddof=0)  # Population standard deviation
    min_volume = np.min(arr)
    max_volume = np.max(arr)
    
    return {
        'total_volume': total_volume,
        'mean_volume': mean_volume,
        'std_deviation': std_deviation,
        'min_volume': min_volume,
        'max_volume': max_volume
    }

def simulate_large_scale_data(size: int = 10_000) -> np.ndarray:
    """
    Generates a large array of random volume measurements to demonstrate performance.
    
    Parameters:
        size (int): Number of elements in the generated array.
        
    Returns:
        np.ndarray: Array of random float values representing volumes.
    """
    # Generate data uniformly distributed between 0 and 1, scaled by a base factor
    base_volume = 500.0
    return (np.random.rand(size) * base_volume).astype(np.float64)

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user input or files
    sample_volumes = np.array([123.4, 456.789, -0.01, 9999.9], dtype=np.float64)

    print("Sample Input Data:")
    print(sample_volumes)

    # Perform vectorized calculations on sample data
    metrics_sample = calculate_volume_metrics(sample_volumes)
    
    print("\nMetrics for Sample Data:")
    for key, value in metrics_sample.items():
        print(f"{key}: {value}")

    # Demonstrate scaling performance with a larger dataset
    large_data_size = 1_000_000
    print(f"\nSimulating scale operation on array size: {large_data_size:,} elements...")
    
    start_time = np.time_ns()
    large_volumes = simulate_large_scale_data(large_data_size)
    end_time_sample_gen = np.time_ns()

    metrics_large = calculate_volume_metrics(large_volumes)
    end_time_calc = np.time_ns()

    elapsed_generation_ms = (end_time_sample_gen - start_time) / 1_000_000.0
    elapsed_calculation_ms = (end_time_calc - end_time_sample_gen) / 1_000_000.0
    
    print(f"Data generation time: {elapsed_generation_ms:.4f} ms")
    print(f"Calculation time for {large_data_size:,} elements: {elapsed_calculation_ms:.4f} ms")

    print("\nMetrics for Large Scale Data:")
    print(f"Total Volume (approx): {metrics_large['total_volume']:.2e}")
    print(f"Mean Volume (approx): {metrics_large['mean_volume']:.2f}")
    print(f"Std Deviation (approx): {metrics_large['std_deviation']:.2f}")