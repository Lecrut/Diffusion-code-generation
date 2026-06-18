import numpy as np

def calculate_volume_metrics(volumes):
    """
    Performs vectorized calculations on an array of volume measurements.
    
    Parameters:
        volumes (np.ndarray or list): Array of volume values.
        
    Returns:
        dict: Dictionary containing calculated metrics including mean, std dev, 
              min, max, and total sum.
    """
    # Convert input to numpy array for vectorized operations if not already an ndarray
    vol_array = np.asarray(volumes)
    
    # Vectorized calculations using NumPy functions which are highly optimized
    result = {
        'mean': np.mean(vol_array),
        'std_deviation': np.std(vol_array, ddof=0),  # Population standard deviation
        'min_volume': np.min(vol_array),
        'max_volume': np.max(vol_array),
        'total_sum': np.sum(vol_array)
    }
    
    return result

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user input or external dependencies
    sample_volumes = [10.5, 23.7, 45.2, 12.8, 67.9]
    
    print("Input Volume Measurements:", sample_volumes)
    
    # Perform calculations using the module function
    metrics = calculate_volume_metrics(sample_volumes)
    
    # Display results in a formatted manner
    for key, value in metrics.items():
        if isinstance(value, float):
            print(f"{key.capitalize()}: {value:.2f}")
        else:
            print(f"{key.capitalize()}: {int(value)}")