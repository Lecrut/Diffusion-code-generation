import math

def compare_complex_magnitudes(z1_real, z1_imag, z2_real, z2_imag):
    """
    Compares the squared magnitudes of two complex numbers without computing square roots.
    
    Parameters:
        z1_real (float): Real part of first complex number
        z1_imag (float): Imaginary part of first complex number
        z2_real (float): Real part of second complex number
        z2_imag (float): Imaginary part of second complex number
        
    Returns:
        int: 1 if |z1| > |z2|, -1 if |z1| < |z2|, 0 otherwise
    """
    sq_mag_1 = z1_real ** 2 + z1_imag ** 2
    sq_mag_2 = z2_real ** 2 + z2_imag ** 2
    
    # Direct comparison of squared magnitudes avoids unnecessary sqrt operations
    if sq_mag_1 > sq_mag_2:
        return 1
    elif sq_mag_1 < sq_mag_2:
        return -1
    else:
        return 0

if __name__ == '__main__':
    # Hard-coded sample values for testing
    z1 = complex(3, 4)      # |z1| = 5 -> squared magnitude = 25
    z2 = complex(-6, -8)   # |z2| = 10 -> squared magnitude = 100
    
    result = compare_complex_magnitudes(z1.real, z1.imag, z2.real, z2.imag)