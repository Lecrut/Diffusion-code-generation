import math

def compare_magnitudes(z1_real: float, z1_imag: float, z2_real: float, z2_imag: float) -> str:
    """
    Compares the magnitudes of two complex numbers by calculating their squared magnitudes.
    
    Args:
        z1_real (float): Real part of first complex number.
        z1_imag (float): Imaginary part of first complex number.
        z2_real (float): Real part of second complex number.
        z2_imag (float): Imaginary part of second complex number.
    
    Returns:
        str: Description of the comparison result ('z1 is larger', 'z2 is larger', or 'equal').
    """
    # Calculate squared magnitudes directly to avoid potential floating-point precision errors from sqrt,
    # and improve computational efficiency by skipping square roots unless explicitly needed.
    mag_sq_z1 = z1_real ** 2 + z1_imag ** 2
    mag_sq_z2 = z2_real ** 2 + z2_imag ** 2
    
    if mag_sq_z1 > mag_sq_z2:
        return "z1 is larger"
    elif mag_sq_z2 > mag_sq_z1:
        return "z2 is larger"
    else:
        # Calculate actual magnitudes only for the 'equal' case to demonstrate usage of math.sqrt if needed,
        # though not strictly necessary for the comparison logic itself.
        mag_z1 = math.sqrt(mag_sq_z1)
        mag_z2 = math.sqrt(mag_sq_z2)
        return f"Equal: |z1|={mag_z1}, |z2|={mag_z2}"

if __name__ == '__main__':
    # Hard-coded sample values for testing without external input or files.
    z1_real = 3.0
    z1_imag = 4.0
    
    z2_real = -5.0
    z2_imag = 12.0

    result = compare_magnitudes(z1_real, z1_imag, z2_real, z2_imag)
    print(result)