import math

def compare_complex_magnitude(z1_real: float, z1_imag: float, z2_real: float, z2_imag: float) -> str:
    """
    Compares the magnitudes of two complex numbers by comparing their squared magnitudes.
    
    Args:
        z1_real (float): Real part of first complex number.
        z1_imag (float): Imaginary part of first complex number.
        z2_real (float): Real part of second complex number.
        z2_imag (float): Imaginary part of second complex number.
    
    Returns:
        str: A string indicating which magnitude is larger, or if they are equal.
             - "z1 > z2" if |z1|² > |z2|²
             - "z2 > z1" if |z2|² > |z1|²
             - "Equal" if |z1|² == |z2|²
    """
    # Calculate squared magnitudes directly to avoid expensive square root operations.
    mag_sq_z1 = z1_real ** 2 + z1_imag ** 2
    mag_sq_z2 = z2_real ** 2 + z2_imag ** 2
    
    if mag_sq_z1 > mag_sq_z2:
        return "z1 > z2"
    elif mag_sq_z2 > mag_sq_z1:
        return "z2 > z1"
    else:
        return "Equal"

if __name__ == '__main__':
    # Hard-coded sample values for testing.
    # z1 = 3 + 4j, |z1|² = 9 + 16 = 25 => |z1| = 5
    a = 3.0
    b = 4.0
    
    # z2 = 5 + 0j, |z2|² = 25 + 0 = 25 => |z2| = 5
    c = 5.0
    d = 0.0
    
    result = compare_complex_magnitude(a, b, c, d)
    
    # Optional: Verify with actual square roots for clarity in the sample output context, 
    # though the comparison logic itself avoids sqrt calls as per optimization requirement.
    z1_mag = math.sqrt(mag_sq_z1) if mag_sq_z1 >= 0 else complex(0, -math.sqrt(-mag_sq_z1))
    z2_mag = math.sqrt(mag_sq_z2) if mag_sq_z2 >= 0 else complex(0, -math.sqrt(-mag_sq_z2))

    print(f"z1 ({a} + {b}j): Squared Magnitude = {mag_sq_z1}, Actual Magnitude ≈ {abs(z1_mag)}")
    print(f"z2 ({c} + {d}j): Squared Magnitude = {mag_sq_z2}, Actual Magnitude ≈ {abs(z2_mag)}")
    print(f"Comparison Result: {result}")