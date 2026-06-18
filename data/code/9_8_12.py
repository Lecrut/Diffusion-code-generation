import numpy as np

def convert_volume(volume_liters: np.ndarray) -> tuple[np.ndarray, str]:
    """
    Converts a NumPy array of volumes from liters to cubic meters using vectorized operations.
    
    Args:
        volume_liters (np.ndarray): Input array containing volume measurements in liters.
        
    Returns:
        tuple: A tuple containing the converted array in cubic meters and a status message.
    """
    # Conversion factor: 1 liter = 0.001 cubic meter
    conversion_factor = np.array([0.001])
    
    # Vectorized multiplication to convert all values at once
    volume_cubic_meters = volume_liters * conversion_factor
    
    return volume_cubic_meters, "Conversion successful"

if __name__ == '__main__':
    # Hard-coded sample data representing 5 measurements in liters
    samples_liters = np.array([10.5, 250.0, 3.75, 1000.0, 0.0])
    
    converted_array, status_message = convert_volume(samples_liters)
    
    print(f"Status: {status_message}")
    print("Original values (Liters):", samples_liters)
    print("Converted values (Cubic Meters):", converted_array)