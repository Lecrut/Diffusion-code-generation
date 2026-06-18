import math

def compare_magnitude_squared(z1_real, z1_imag, z2_real, z2_imag):
    """
    Compares the squared magnitudes of two complex numbers without computing square roots.
    
    Parameters:
        z1_real (float or int): Real part of first complex number a in a + bi
        z1_imag (float or int): Imaginary part of first complex number b in a + bi
        z2_real (float or int): Real part of second complex number c in c + di
        z2_imag (float or int): Imaginary part of second complex number d in c + di
    
    Returns:
        str: 'z1_greater' if |z1| > |z2|, 
             'z2_greater' if |z2| > |z1|, 
             'equal' otherwise.
    
    Note: Comparing squared magnitudes (a^2 + b^2 vs c^2 + d^2) is mathematically equivalent
          to comparing actual magnitudes and avoids expensive square root operations for efficiency.
    """
    mag_sq_z1 = z1_real ** 2 + z1_imag ** 2
    mag_sq_z2 = z2_real ** 2 + z2_imag ** 2

    if mag_sq_z1 > mag_sq_z2:
        return 'z1_greater'
    elif mag_sq_z2 > mag_sq_z1:
        return 'z2_greater'
    else:
        return 'equal'

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    z1 = 3 + 4j   # |z1|^2 = 9 + 16 = 25, actual magnitude = 5.0
    z2 = 1 + j    # |z2|^2 = 1 + 1 = 2, actual magnitude ≈ 1.414

    result = compare_magnitude_squared(z1.real, z1.imag, z2.real, z2.imag)
    
    print(f"Complex number z1: {z1}")
    print(f"Squared magnitude of z1 ({z1.real}^2 + {z1.imag}^2): {3**2 + 4**2}")

    print(f"\nComplex number z2: {z2}")
    print(f"Squared magnitude of z2 ({z2.real}^2 + {z2.imag}^2): {1**2 + 1**2}")

    if result == 'equal':
        print("\nThe magnitudes are equal.")
    elif result == 'z1_greater':
        print("\nMagnitude of z1 is greater than magnitude of z2.")
    else:
        print("\nMagnitude of z2 is greater than magnitude of z1.")

    # Optional verification using math.sqrt for clarity (not used in comparison logic)
    mag_z1 = math.sqrt(3**2 + 4**2)
    mag_z2 = math.sqrt(1**2 + 1**2)
    print(f"\nVerification with actual magnitudes: |z1|={mag_z1}, |z2|≈{mag_z2:.5f}")