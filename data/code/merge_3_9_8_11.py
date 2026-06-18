import numpy as np

def convert_volume(volume_liters: np.ndarray) -> tuple[np.ndarray, str]:
    """
    Converts a NumPy array of volumes from liters to cubic meters using vectorized operations.
    
    Parameters:
        volume_liters (np.ndarray): Input array of values in liters.
        
    Returns:
        tuple: A tuple containing the converted array and a status message.
    """
    # Conversion factor: 1 liter = 0.001 cubic meters
    conversion_factor = np.array([0.001])
    
    # Perform vectorized multiplication to convert liters to cubic meters
    volume_cubic_meters = volume_liters * conversion_factor
    
    return volume_cubic_meters, "Conversion successful"

if __name__ == '__main__':
    # Hard-coded sample values for demonstration purposes.
    # These represent a list of water tank capacities in liters.
    input_data = np.array([100, 500, 2500, 75])

    print("Input Volume (Liters):", input_data)

    converted_array, status_message = convert_volume(input_data)

    print(f"Status: {status_message}")
    print("Converted Volume (Cubic Meters):", converted_array)