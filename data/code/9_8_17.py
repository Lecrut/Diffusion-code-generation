import numpy as np

def convert_volume(input_array):
    """
    Converts volume measurements from cubic meters to liters using NumPy vectorization.
    
    Parameters:
        input_array (np.ndarray or list-like): Array of volumes in cubic meters.
        
    Returns:
        np.ndarray: Volumes converted to liters.
    """
    # Vectorized conversion factor: 1 m^3 = 1000 L
    return input_array * 1000

if __name__ == '__main__':
    # Hard-coded sample values (cubic meters)
    measurements_cubed_meters = [5.2, 10.5, 0.75, 3.0]

    # Convert to NumPy array for vectorized operations
    volumes_array = np.array(measurements_cubed_meters)

    # Perform bulk conversion using the function (vectorized via multiplication in numpy context or explicit return)
    converted_liters = convert_volume(volumes_array)

    print("Original measurements (m³):", volumes_array)
    print("Converted to liters:", converted_liters)