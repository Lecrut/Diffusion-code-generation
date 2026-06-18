import math

def compare_magnitudes_squared(z1: tuple[float, float], z2: tuple[float, float]) -> str:
    """
    Compare the magnitude of two complex numbers represented as tuples (a, b) and (c, d).
    
    Returns a string indicating which squared magnitude is larger.
    
    Args:
        z1: Tuple containing real part 'a' and imaginary part 'b'.
        z2: Tuple containing real part 'c' and imaginary part 'd'.
        
    Returns:
        A message describing the comparison result without computing square roots for efficiency.
    """
    # Compute squared magnitudes directly to avoid expensive sqrt operations during comparison
    mag_sq_z1 = z1[0] ** 2 + z1[1] ** 2
    mag_sq_z2 = z2[0] ** 2 + z2[1] ** 2

    if mag_sq_z1 > mag_sq_z2:
        return f"z1 ({z1}) has a greater magnitude than z2 ({z2}). Squared magnitudes: {mag_sq_z1} vs {mag_sq_z2}"
    elif mag_sq_z2 > mag_sq_z1:
        return f"z2 ({z2}) has a greater magnitude than z1 ({z1}). Squared magnitudes: {mag_sq_z2} vs {mag_sq_z1}"
    else:
        return f"Magnitudes are equal. Both have squared magnitude of {mag_sq_z1}. Values represented as complex numbers would be " + \
               str(complex(z1[0], z1[1])) + " and " + str(complex(z2[0], z2[1]))

if __name__ == '__main__':
    # Hard-coded sample values ensuring no user input or external dependencies are needed.
    z_1_real, z_1_imag = 3, 4          # |z1|^2 = 9 + 16 = 25 -> |z1| = 5.0
    z_2_real, z_2_imag = -sqrt(8), sqrt(7)  # |z2|^2 ~ 16.34
    
    from math import sqrt

    result_z_equal = compare_magnitudes_squared(z_1, z_2)
    
    print(result_z_equal)