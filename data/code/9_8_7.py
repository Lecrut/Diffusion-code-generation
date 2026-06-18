import numpy as np

def convert_volumes(volume_array: np.ndarray) -> tuple[np.ndarray, str]:
    """
    Performs vectorized volume conversions (Liters to Cubic Meters) on an entire array.
    
    Args:
        volume_array: A NumPy array of values in Liters.
        
    Returns:
        A tuple containing the converted array and a conversion factor string.
    """
    # Conversion factor from Liters to Cubic Meters (1 L = 0.001 m³)
    factor = 1e-3
    
    result = volume_array * factor
    return result, f"{factor} cubic meters per liter"

if __name__ == '__main__':
    # Hard-coded sample values representing measurements in Liters
    sample_measurements_liters = np.array([50.0, 120.5, -10.3], dtype=float)
    
    print("Input Measurements (Liters):")
    print(sample_measurements_liters)
    
    converted_array, conversion_info = convert_volumes(sample_measurements_liters)
    
    print("\nConverted to Cubic Meters:")
    print(converted_array)
    print(f"\nConversion Factor: {conversion_info}")