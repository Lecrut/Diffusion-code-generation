import math

def compare_magnitude_z1(z1_real, z1_imag, z2_real, z2_imag):
    """
    Compares the magnitude of two complex numbers by comparing their squared magnitudes.
    
    Parameters:
        z1_real (float or int): Real part of first complex number a in a + bi
        z1_imag (float or int): Imaginary part of first complex number b in a + bi
        z2_real (float or int): Real part of second complex number c in c + di
        z2_imag (float or int): Imaginary part of second complex number d in c + di
        
    Returns:
        str: 'z1' if |z1| > |z2|, 'z2' if |z2| > |z1|, 'equal' otherwise
    """
    # Calculate squared magnitudes directly to avoid square roots for comparison efficiency
    mag_sq_z1 = z1_real ** 2 + z1_imag ** 2
    mag_sq_z2 = z2_real ** 2 + z2_imag ** 2
    
    if mag_sq_z1 > mag_sq_z2:
        return 'z1'
    elif mag_sq_z2 > mag_sq_z1:
        return 'z2'
    else:
        return 'equal'

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    a, b = 3.0, 4.0   # z1 = 3 + 4i -> |z1|^2 = 9 + 16 = 25
    c, d = 1.0, -2.0  # z2 = 1 - 2i -> |z2|^2 = 1 + 4 = 5
    
    result = compare_magnitude_z1(a, b, c, d)
    
    print(f"Comparing magnitudes of z1={a}+{b}j and z2={c}+{d}j")
    if result == 'z1':
        print("Result: |z1| is greater than |z2|")
    elif result == 'z2':
        print("Result: |z2| is greater than |z1|")
    else:
        print("Result: Magnitudes are equal")

    # Optional verification with actual roots for clarity (not used in comparison logic)
    mag_z1 = math.sqrt(a**2 + b**2)
    mag_z2 = math.sqrt(c**2 + d**2)
    print(f"Verification: |z1| = {mag_z1}, |z2| = {mag_z2}")