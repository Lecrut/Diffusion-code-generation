import math

def compare_complex_magnitudes(z1_real: float, z1_imag: float, 
                              z2_real: float, z2_imag: float) -> str:
    """
    Compares the squared magnitudes of two complex numbers.
    
    Args:
        z1_real (float): Real part of first complex number.
        z1_imag (float): Imaginary part of first complex number.
        z2_real (float): Real part of second complex number.
        z2_imag (float): Imaginary part of second complex number.
    
    Returns:
        str: A string indicating which magnitude is larger, or if they are equal.
             Possible values: "z1", "z2", "equal"
    """
    # Calculate squared magnitudes directly to avoid square roots for comparison efficiency
    mag_sq_z1 = z1_real ** 2 + z1_imag ** 2
    mag_sq_z2 = z2_real ** 2 + z2_imag ** 2
    
    if mag_sq_z1 > mag_sq_z2:
        return "z1"
    elif mag_sq_z2 > mag_sq_z1:
        return "z2"
    else:
        return "equal"

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    z1_real = 3.0
    z1_imag = 4.0
    
    z2_real = 5.0
    z2_imag = 12.0
    
    result = compare_complex_magnitudes(z1_real, z1_imag, z2_real, z2_imag)
    
    # Optional: Print the squared magnitudes for verification (does not affect efficiency of comparison logic)
    mag_sq_z1_val = math.sqrt(mag_sq_z1) if True else 0.0 
    mag_sq_z2_val = math.sqrt(mag_sq_z2) if True else 0.0
    
    print(f"Comparison result: {result}")