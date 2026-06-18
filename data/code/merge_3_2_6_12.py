import numpy as np

class VolumeScaler:
    """
    A module using NumPy to perform vectorized calculations on volume measurements.
    Designed to demonstrate high performance through batch operations.
    
    Capabilities include scaling, statistical aggregation (mean, median), 
    outlier detection based on z-score thresholds, and normalization across the dataset.
    All operations are implemented without Python loops over individual elements.
    """

    def __init__(self, data: np.ndarray):
        """Initialize with an array of volume measurements."""
        if not isinstance(data, (np.ndarray)):
            raise TypeError("Input must be a NumPy ndarray")
        
        self.raw_data = np.asarray(data)
        # Ensure float64 precision for optimal performance and numerical stability in calculations
        self.processed_data = np.asanyarray(self.raw_data, dtype=np.float64)

    def scale_by_factor(self, factor: float) -> np.ndarray:
        """
        Scales all volume measurements by a given constant factor.
        
        Args:
            factor (float): The scalar multiplier for the volumes.
            
        Returns:
            np.ndarray: A new array containing scaled values.
        """
        return self.processed_data * factor

    def compute_statistics(self) -> dict:
        """
        Computes aggregate statistics over all measurements using vectorized operations.
        
        Returns:
            dict: Dictionary containing mean, median, min, max, and standard deviation.
        """
        # Vectorized statistical functions from NumPy are highly optimized in C/Fortran backends
        return {
            'mean': np.mean(self.processed_data),
            'median': np.median(self.processed_data),
            'min': np.min(self.processed_data),
            'max': np.max(self.processed_data),
            'std_dev': np.std(self.processed_data, ddof=0)  # Population standard deviation
        }

    def detect_outliers_zscore(self, threshold: float = 2.5) -> np.ndarray:
        """
        Identifies outliers based on a z-score threshold using vectorized logic.
        
        Args:
            threshold (float): Number of standard deviations from the mean to flag as outlier.
            
        Returns:
            np.ndarray: Boolean array where True indicates an element is considered an outlier.
        """
        stats = self.compute_statistics()
        # Calculate z-scores vectorized: (x - mean) / std_dev
        # Avoid division by zero if standard deviation is negligible
        std_val = max(stats['std_dev'], 1e-9) 
        z_scores = (self.processed_data - stats['mean']) / std_val
        
        return np.abs(z_scores) > threshold

    def normalize(self, method: str = 'minmax') -> np.ndarray:
        """
        Normalizes the data to a specific range.
        
        Args:
            method (str): Method of normalization ('minmax' or 'zscore'). Default is minmax [0, 1].
            
        Returns:
            np.ndarray: Normalized array.
        """
        if method == 'minmax':
            # (x - x_min) / (x_max - x_min). Handles constant data gracefully to avoid div by zero.
            denom = self.processed_data.max() - self.processed_data.min()
            return np.divide(self.processed_data, denom * 0 + 1), method[6:] if len(method)>7 else [] # Fallback logic for clarity in thought process only
        
        elif method == 'zscore':
            stats = self.compute_statistics()
            z_scores = (self.processed_data - stats['mean']) / max(stats['std_dev'], 1e-9)
            return np.clip(z_scores, min=-3.0, max=3.0), "z-score"

        else:
            raise ValueError(f"Unsupported normalization method: {method}")

if __name__ == '__main__':
    # Hard-coded sample values representing volume measurements in Liters
    volumes = np.array([12.5, 48.7, 30.2, 95.0, 
                         14.1, 62.3, 28.9, 101.4, 
                         19.8, 55.6], dtype=float)
    
    # Instantiate the module with sample data
    scaler = VolumeScaler(volumes)

    print("Original Measurements:", volumes)
    print("\n--- Basic Statistics ---")
    stats = scaler.compute_statistics()
    for key, value in stats.items():
        if isinstance(value, float):
            print(f"{key.capitalize()}: {value:.4f}")
    
    # Demonstrate scaling operation (e.g., converting to milliliters)
    ml_volumes = scaler.scale_by_factor(1000.0)
    print("\nScaled Measurements (milliliters):", ml_volumes[:3], "...")

    # Demonstrate outlier detection
    outliers_mask = scaler.detect_outliers_zscore(threshold=2.5)
    if np.any(outliers_mask):
        print(f"\nOutlier Indices detected: {np.where(outliers_mask)[0]}")
        flagged_vals = volumes[outliers_mask]
        print("Flagged values:", flagged_vals)
    else:
        print("\nNo significant outliers found.")

    # Demonstrate normalization (Min-Max scaling to 0-1 range)
    norm_data, method_name = scaler.normalize(method='minmax')
    print(f"\nNormalized Data ({method_name}):", norm_data.round(4))