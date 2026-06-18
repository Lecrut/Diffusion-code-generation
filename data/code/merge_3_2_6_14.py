import numpy as np

def calculate_volume_metrics(volumes):
    """
    Perform vectorized calculations on an array of volume measurements.
    
    Parameters:
        volumes (np.ndarray or list): Array containing numerical volume values.
        
    Returns:
        dict: A dictionary containing the following metrics:
            - mean_volume: The arithmetic mean of all volumes.
            - median_volume: The statistical median of the volumes.
            - total_volume: Sum of all individual volume measurements.
            - standard_deviation: Population standard deviation (ddof=0).
            - variance: Population variance.
    """
    # Convert input to numpy array if it isn't already for consistent behavior
    arr = np.asarray(volumes, dtype=float)
    
    mean_vol = np.mean(arr)
    median_vol = np.median(arr)
    total_vol = np.sum(arr)
    std_dev = np.std(arr, ddof=0)  # Population standard deviation
    variance = np.var(arr, ddof=0)   # Population variance
    
    return {
        'mean_volume': mean_vol,
        'median_volume': median_vol,
        'total_volume': total_vol,
        'standard_deviation': std_dev,
        'variance': variance
    }

if __name__ == '__main__':
    # Hard-coded sample volume measurements in cubic meters (m³)
    raw_data = [10.5, 23.7, 15.2, 48.9, 12.1, 
                 67.3, 34.5, 8.2, 55.6, 29.4]
    
    # Convert to NumPy array for vectorized processing
    volumes_array = np.array(raw_data)
    
    print("Input Volume Measurements (m³):", raw_data)
    metrics = calculate_volume_metrics(volumes_array)
    
    results = {k: float(round(v, 4)) for k, v in metrics.items()}
    print("\nCalculated Metrics:")
    for key, value in results.items():
        print(f"  {key}: {value}")
        
    # Demonstrate scaling performance with a larger synthetic dataset
    large_dataset = np.random.uniform(5.0, 100.0, size=1_000_000)
    
    print("\nPerformance Test on Large Dataset (1 million elements)...")
    start_time = __import__('time').performance() if hasattr(__import__("time"), "performance") else __import__("time").time_ns
    
    # Perform calculation again on the large dataset to verify scaling capability
    _ = calculate_volume_metrics(large_dataset)
    
    end_time = (start_type := None).replace(start_time, __import__('time').time() * 10**9) if start_time is not None else __import__("time").time_ns
    
    print("Vectorized calculation completed successfully for the large dataset.")