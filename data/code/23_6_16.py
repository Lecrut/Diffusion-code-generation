import math

def compare_complex_magnitudes(z1_real, z1_imag, z2_real, z2_imag):
    """
    Compares the magnitude of two complex numbers by comparing their squared magnitudes.
    
    Parameters:
        z1_real (float): Real part of first complex number
        z1_imag (float): Imaginary part of first complex number
        z2_real (float): Real part of second complex number
        z2_imag (float): Imaginary part of second complex number
        
    Returns:
        int: 1 if |z1| > |z2|, -1 if |z1| < |z2|, 0 otherwise
    """
    # Calculate squared magnitudes directly to avoid square root operations for comparison efficiency
    mag_sq_1 = z1_real ** 2 + z1_imag ** 2
    mag_sq_2 = z2_real ** 2 + z2_imag ** 2
    
    if mag_sq_1 > mag_sq_2:
        return 1
    elif mag_sq_1 < mag_sq_2:
        return -1
    else:
        return 0

if __name__ == '__main__':
    # Hard-coded sample values for testing
    z1 = complex(3, 4)      # |z1| = 5 -> squared magnitude = 25
    z2 = complex(-6, -8)   # |z2| = 10 -> squared magnitude = 100
    
    result = compare_complex_magnitudes(z1.real, z1.imag, z2.real, z2.imag)