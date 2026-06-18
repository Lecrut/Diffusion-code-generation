import math

def compare_magnitude_z1(z1_real: float, z1_imag: float, 
                         z2_real: float, z2_imag: float) -> str:
    """
    Compare the magnitude of two complex numbers by comparing their squared magnitudes.
    
    Parameters:
        z1_real (float): Real part of first complex number.
        z1_imag (float): Imaginary part of first complex number.
        z2_real (float): Real part of second complex number.
        z2_imag (float): Imaginary part of second complex number.
    
    Returns:
        str: Description of which magnitude is larger or if they are equal.
    """
    # Calculate squared magnitudes to avoid square root operations for efficiency
    sq_mag_z1 = z1_real ** 2 + z1_imag ** 2
    sq_mag_z2 = z2_real ** 2 + z2_imag ** 2
    
    comparison_result = ""
    
    if sq_mag_z1 > sq_mag_z2:
        comparison_result = f"z1 ({z1_real}+{z1_imag}j) has a greater magnitude than z2 ({z2_real}+{z2_imag}j)."
    elif sq_mag_z1 < sq_mag_z2:
        comparison_result = f"z2 ({z2_real}+{z2_imag}j) has a greater magnitude than z1 ({z1_real}+{z1_imag}j)."
    else:
        # Compute actual magnitudes only if needed for display, though squared values are equal
        mag_z1 = math.sqrt(sq_mag_z1)
        comparison_result = f"Both complex numbers have the same magnitude: {mag_z1:.4f}"
    
    return comparison_result

if __name__ == '__main__':
    # Hard-coded sample values for testing without any user input or external dependencies
    
    z1_real, z1_imag = 3.0, 4.0   # |z1| = 5.0 -> sq_mag = 25.0
    z2_real, z2_imag = -1.0, 7.0  # |z2| ≈ 6.98 -> sq_mag = 50.0
    
    result_str = compare_magnitude_z1(z1_real, z1_imag, z2_real, z2_imag)
    
    print(result_str)