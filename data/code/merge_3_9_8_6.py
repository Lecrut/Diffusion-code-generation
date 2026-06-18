import numpy as np

def convert_volumes(volume_array: np.ndarray) -> dict[str, float]:
    """
    Performs vectorized volume conversions from cubic centimeters (cm3) 
    to liters (L), milliliters (mL), and US fluid ounces (fl oz).
    
    Conversion factors applied element-wise using NumPy broadcasting.
    1 cm³ = 0.001 L
    1 cm³ = 1 mL
    1 cm³ ≈ 0.033814 fl oz
    
    Args:
        volume_array (np.ndarray): Input array of values in cubic centimeters.
        
    Returns:
        dict[str, float]: Dictionary containing converted volumes for each unit type.
    """
    
    # Define conversion factors relative to the input unit (cm³)
    factor_l = 0.001       # Convert cm³ to liters
    factor_ml = 1.0        # Convert cm³ to milliliters (numerically equal)
    factor_fl_oz = 0.033814 # Convert cm³ to US fluid ounces
    
    input_values = volume_array.astype(np.float64).ravel()
    
    converted_liters = input_values * factor_l
    converted_mL = input_values * factor_ml
    converted_floz = input_values * factor_fl_oz
    
    return {
        'input_unit': 'cm³',
        'input_sum': np.sum(input_values),
        'output_L': float(np.round(converted_liters, 6)),
        'output_mL': float(np.round(converted_mL, 2)),
        'output_fl_oz': float(np.round(converted_floz, 4))
    }

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    # Example: Array of volumes in cubic centimeters provided by the "user" scenario
    raw_measurements = np.array([10.5, 23.7, 45.8]) 
    
    results = convert_volumes(raw_measurements)
    
    print(f"Input Measurements (cm³): {raw_measurements}")
    print("Converted Volumes:")
    print(f"\nSum of input: {results['input_sum']} cm³")
    print("-"*40)
    print(f"Liters (L):\t\t{float(results['output_L'])} L")
    print(f"Milliliters (mL): \t{float(results['output_mL'])} mL")
    print(f"\nUS Fluid Ounces: {results['input_sum'] * 0.033814:.2f}")