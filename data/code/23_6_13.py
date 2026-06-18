import math

def compare_complex_magnitude(z1_a: float, z1_b: float, z2_c: float, z2_d: float) -> str:
    """
    Compare the magnitude of two complex numbers by comparing their squared magnitudes.
    
    Parameters:
        z1_a (float): Real part of first complex number
        z1_b (float): Imaginary part of first complex number
        z2_c (float): Real part of second complex number
        z2_d (float): Imaginary part of second complex number
    
    Returns:
        str: Description of the comparison result ('z1 larger', 'equal', or 'z2 larger')
    
    Note: Squared magnitudes are compared directly to avoid computationally expensive square root operations.
    """
    mag_sq_z1 = z1_a ** 2 + z1_b ** 2
    mag_sq_z2 = z2_c ** 2 + z2_d ** 2

    if math.isclose(mag_sq_z1, mag_sq_z2):
        return "Equal magnitude"
    elif mag_sq_z1 > mag_sq_z2:
        return "z1 has larger magnitude"
    else:
        return "z2 has larger magnitude"

if __name__ == '__main__':
    # Hard-coded sample values for testing (no user input required)
    a, b = 3.0, 4.0       # z1 = 3 + 4i -> |z1|^2 = 25
    c, d = 5.0, -12.0     # z2 = 5 - 12i -> |z2|^2 = 169
    
    result_str = compare_complex_magnitude(a, b, c, d)
    
    print(f"Comparing complex numbers: ({a} + {b}j) vs ({c} + {d}j)")
    print(f"Squared magnitudes comparison result: {result_str}")

    # Optional demonstration of actual magnitude calculation if needed for verification
    mag1 = math.sqrt(a**2 + b**2)
    mag2 = math.sqrt(c**2 + d**2)
    print(f"Actual |z1| = {mag1}, Actual |z2| = {mag2}")

    # Additional test case to verify equality logic
    a_test, b_test = 1.0, 1.0      # z3 = 1+i -> |z|^2 = 2