import numpy as np

def convert_volume_array(volume_input: np.ndarray) -> tuple[np.ndarray, dict]:
    """
    Performs vectorized volume conversions from cubic meters to liters and gallons (US).
    
    Args:
        volume_input: A NumPy array of values in cubic meters.
        
    Returns:
        A tuple containing:
            - numpy_array_liters: Converted volumes in liters.
            - info_dict: Dictionary with conversion factors used.
    """
    # Define conversion constants for vectorized operations
    m3_to_liter = 1000.0          # 1 cubic meter = 1000 liters
    m3_to_gallon_us = 264.172052   # 1 cubic meter ≈ 264.17 US gallons
    
    # Perform vectorized conversion to liters and US gallons using NumPy arithmetic
    volumes_liters = volume_input * m3_to_liter
    volumes_gallons_us = volume_input * m3_to_gallon_us
    
    info_dict = {
        "input_unit": "cubic_meters",
        "output_units": ["liters", "gallons_us"],
        "factors_used": {"liter_per_m3": m3_to_liter, "galus_per_m3": m3_to_gallon_us}
    }
    
    return volumes_liters, info_dict

if __name__ == '__main__':
    # Hard-coded sample values for testing efficiency and correctness
    # Simulating an array of 10 measurements in cubic meters between 0.5 and 2.0 m³
    raw_measurements = np.array([0.5, 0.75, 1.0, 1.25, 1.5, 
                                  1.75, 2.0]) * 10 / 3 + 0.4
    
    # Convert array to float64 for optimal performance
    input_array = raw_measurements.astype(np.float64)
    
    print("Input Measurements (m³):")
    print(input_array)
    
    liters, info_dict = convert_volume_array(input_array)
    
    print("\nConversion Factors Used:")
    print(info_dict["factors_used"])
    
    print("\nConverted Volumes in Liters:")
    print(liters)
    
    gallons_us = input_array * info_dict["factors_used"]["galus_per_m3"]
    print("Converted Volumes (US Gallons):")
    print(gallons_us)