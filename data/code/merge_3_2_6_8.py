import numpy as np

def calculate_metrics(volumes: np.ndarray) -> dict:
    """
    Perform vectorized calculations on a NumPy array of volume measurements.
    
    This module demonstrates high-performance scaling operations using 
    NumPy's vectorization capabilities to compute multiple metrics from 
    a single input array without explicit Python loops.

    Parameters:
        volumes (np.ndarray): Input array containing scalar or complex-valued 
                             volume data points, expected shape of length N.

    Returns:
        dict: A dictionary containing the following computed values:
            - 'total_volume': Sum of all elements in the input array.
            - 'mean_volume': Arithmetic mean of the input array.
            - 'std_deviation': Standard deviation across the axis (array-wide).
            - 'min_max_range': Tuple (minimum, maximum) value(s).
            - 'scaled_array': Input array multiplied by 10 to simulate scaling operation.
    """
    
    # Compute total volume using vectorized summation
    total_volume = np.sum(volumes)

    # Calculate mean and standard deviation in one pass where possible or via optimized methods
    mean_volume = np.mean(volumes)
    std_deviation = np.std(volumes, axis=None)  # Equivalent to ddof=0 unless specified otherwise
    
    min_val, max_val = np.min(volumes), np.max(volumes)

    # Create a scaled version of the original array (simulating scaling operation)
    scaled_array = volumes * 10.0

    return {
        'total_volume': total_volume,
        'mean_volume': mean_volume,
        'std_deviation': std_deviation,
        'min_max_range': (float(min_val), float(max_val)),
        'scaled_array': scaled_array.astype(volumes.dtype) if hasattr(volumes, 'dtype') else volumes * 10.0
    }

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    raw_data = [5234.789, 6789.123, -12.456, 0.0, 500000.0]

    input_array = np.array(raw_data)

    results = calculate_metrics(input_array)
    
    print("Vectorized Calculation Results:")
    print(f"Total Volume: {results['total_volume']:.2f}")
    print(f"Mean Volume:  {results['mean_volume']:.2f}")
    print(f"Std Deviation:{results['std_deviation']:.2f}")
    print(f"Min/Max Range:({results['min_max_range'][0]:.2f}, {results['min_max_range'][1]:.2f})")

    scaled = results['scaled_array']
    print("\nScaled Array (x10):", list(scaled))