import math

def compare_complex_magnitudes(z1_real: float, z1_imag: float, 
                              z2_real: float, z2_imag: float) -> str:
    """
    Compare the magnitude of two complex numbers by comparing their squared magnitudes.
    
    Args:
        z1_real (float): Real part of first complex number.
        z1_imag (float): Imaginary part of first complex number.
        z2_real (float): Real part of second complex number.
        z2_imag (float): Imaginary part of second complex number.

    Returns:
        str: A message indicating which magnitude is larger or if they are equal.
    """
    # Calculate squared magnitudes to avoid expensive square root operations for comparison
    sq_mag_1 = z1_real ** 2 + z1_imag ** 2
    sq_mag_2 = z2_real ** 2 + z2_imag ** 2

    if sq_mag_1 > sq_mag_2:
        return "Magnitude of the first complex number is greater."
    elif sq_mag_2 > sq_mag_1:
        return "Magnitude of the second complex number is greater."
    else:
        # Calculate actual magnitudes only when they are equal for completeness, 
        # though strictly not needed if we just want comparison status.
        mag_1 = math.sqrt(sq_mag_1)
        mag_2 = math.sqrt(sq_mag_2)
        return f"Magnitudes are equal: |z1| = {mag_1:.4f} and |z2| = {mag_2:.4f}"

if __name__ == '__main__':
    # Hard-coded sample values for testing
    z1_real, z1_imag = 3.0, 4.0  # Represents complex number (3 + 4j) -> magnitude squared is 9+16=25
    z2_real, z2_imag = -1.0, math.sqrt(8)  # Represents (-1 + j*sqrt(8)) -> magnitude squared is 1+8=9

    result = compare_complex_magnitudes(z1_real, z1_imag, z2_real, z2_imag)
    print(result)