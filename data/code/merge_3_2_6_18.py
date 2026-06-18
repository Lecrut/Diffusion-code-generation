import numpy as np

def calculate_volume_metrics(volumes: list) -> dict:
    """
    Performs vectorized calculations on a list of volume measurements.
    
    Parameters:
        volumes (list): List of float values representing volume measurements.
        
    Returns:
        dict: Dictionary containing computed metrics including mean, std deviation, 
              min/max, and total sum using NumPy operations for performance.
    """
    # Convert input list to a NumPy array for vectorized operations
    vol_array = np.array(volumes)
    
    # Compute basic statistics efficiently without Python loops
    mean_val = np.mean(vol_array)
    std_val = np.std(vol_array, ddof=0)  # Population standard deviation
    min_vol = np.min(vol_array)
    max_vol = np.max(vol_array)
    total_sum = np.sum(vol_array)
    
    return {
        "mean": mean_val,
        "std_deviation": std_val,
        "min_volume": min_vol,
        "max_volume": max_vol,
        "total_volume": total_sum,
        "count": len(vol_array),
        "array_shape": vol_array.shape
    }

if __name__ == '__main__':
    # Hard-coded sample volume measurements (milliliters)
    sample_volumes = [150.5, 230.75, 189.2, 245.6, 175.3, 
                       201.9, 167.4, 223.8, 198.1, 210.4]
    
    # Execute the calculation module
    metrics = calculate_volume_metrics(sample_volumes)
    
    # Display results clearly
    print("Vectorized Volume Measurement Analysis")
    print("=" * 45)
    print(f"Total Measurements: {metrics['count']} items")
    print(f"Array Shape: {metrics['array_shape']}")
    print("-" * 20)
    print(f"Mean Volume:     {metrics['mean']:.2f} mL")
    print(f"Std Deviation:   {metrics['std_deviation']:.2f} mL")
    print(f"Minimum Volume:  {metrics['min_volume']:.2f} mL")
    print(f"Maximum Volume:  {metrics['max_volume']:.2f} mL")
    print("-" * 40)
    print(f"Total Combined:  {metrics['total_volume']:.2f} mL")