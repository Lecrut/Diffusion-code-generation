import numpy as np

def calculate_volume_metrics(volumes):
    """
    Performs vectorized calculations on an array of volume measurements.
    
    Parameters:
        volumes (np.ndarray or list): Array of volume values.
        
    Returns:
        dict: Dictionary containing calculated metrics including mean, median, 
              standard deviation, min, max, and sum.
    """
    # Convert input to numpy array for vectorized operations if not already an ndarray
    arr = np.array(volumes)
    
    # Vectorized calculations using NumPy functions which are highly optimized
    mean_vol = np.mean(arr)
    median_vol = np.median(arr)
    std_dev = np.std(arr, ddof=0)  # Population standard deviation
    min_val = np.min(arr)
    max_val = np.max(arr)
    total_volume = np.sum(arr)
    
    return {
        'mean': mean_vol,
        'median': median_vol,
        'std_deviation': std_dev,
        'minimum': min_val,
        'maximum': max_val,
        'total_sum': total_volume
    }

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user input or external dependencies
    sample_volumes = [10.5, 23.7, 45.2, 89.1, 67.3, 34.8, 12.9, 56.4]
    
    # Perform calculations using the module function
    metrics = calculate_volume_metrics(sample_volumes)
    
    # Output results to demonstrate functionality and performance of vectorized operations
    print("Volume Measurement Analysis Results:")
    for key, value in metrics.items():
        if isinstance(value, float):
            print(f"{key.capitalize()}: {value:.4f}")
        else:
            print(f"{key.capitalize()}: {int(value)}")