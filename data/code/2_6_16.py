import numpy as np

class VolumeScaler:
    """
    A module designed to perform high-performance vectorized calculations on volume measurements using NumPy.
    
    This class demonstrates scaling operations (normalization, transformation) and statistical aggregation
    applied entirely in a vectorized manner without explicit Python loops over the data elements.
    """

    def normalize(self, volumes: np.ndarray, min_val=None, max_val=None):
        """
        Normalize volume measurements to a specified range or [0, 1] interval.
        
        Parameters:
            volumes (np.ndarray): Input array of volume measurements.
            min_val (float): Minimum value for target scaling. Defaults to None (min in data).
            max_val (float): Maximum value for target scaling. Defaults to None (max in data).
            
        Returns:
            np.ndarray: Normalized volumes as a float32 array for memory efficiency.
        """
        if min_val is None or max_val is None:
            # Use the actual minimum and maximum of the dataset dynamically
            min_val, max_val = v.min(), v.max()
        
        range_vals = max_val - min_val
        normalized = (volumes - min_val) / range_vals
        
        return np.asarray(normalized, dtype=np.float32)

    def transform_to_cubic_units(self, volumes: np.ndarray):
        """
        Transform cubic units to liters assuming a base unit conversion factor of 0.1 per dimension.
        
        Parameters:
            volumes (np.ndarray): Input array of volume measurements in original units.
            
        Returns:
            np.ndarray: Transformed volume values using element-wise multiplication by the scaling factor.
        """
        # Assuming cubic scale where dimensions are scaled, a simple scalar multiplier is demonstrated here
        scale_factor = 0.1 ** 3 
        return volumes * scale_factor

    def aggregate_stats(self, volumes: np.ndarray):
        """
        Compute key statistical aggregates (mean, median, std) in vectorized fashion.
        
        Parameters:
            volumes (np.ndarray): Input array of volume measurements.
            
        Returns:
            tuple: A tuple containing mean, median, and standard deviation as floats.
        """
        return float(np.mean(volumes)), float(np.median(volumes)), float(np.std(volumes))

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user input or file I/O
    raw_volumes = np.array([100, 250.5, 375, 499.8, 625], dtype=np.float64)

    scaler = VolumeScaler()

    # Perform normalization to [min, max] range explicitly defined for clarity
    normalized_vol = scaler.normalize(raw_volumes, min_val=100, max_val=625)
    
    # Apply transformation logic (simulated unit conversion)
    transformed_vol = scaler.transform_to_cubic_units(normalized_vol * 625.0)

    # Calculate and display aggregate statistics on the raw data
    mean_v, median_v, std_dev_v = aggregator_stats(raw_volumes)

    print("Normalized Volumes:", normalized_vol.tolist())
    print("Transformed Volumes (scaled):", transformed_vol.tolist())
    print(f"Mean: {mean_v}, Median: {median_v}, Std Dev: {std_dev_v}")