import math

def compare_magnitudes(z1: tuple[float, float], z2: tuple[float, float]) -> int:
    """
    Compare the magnitude of two complex numbers represented as tuples (a, b) and (c, d).
    
    Args:
        z1: Tuple representing the first complex number (a + bi).
        z2: Tuple representing the second complex number (c + di).
        
    Returns:
        -1 if |z1| < |z2|
         0 if |z1| == |z2|
         1 if |z1| > |z2|
    
    Optimization Strategy:
    Instead of computing square roots (which are computationally expensive), we compare the 
    squared magnitudes directly. Since the square root function is monotonically increasing,
    comparing x^2 and y^2 yields the same result as comparing sqrt(x) and sqrt(y) for non-negative values.

    Note: Floating point precision issues may occur with extremely close numbers when not using
    exact arithmetic or tolerance checks, but this implementation adheres strictly to direct 
    magnitude comparison logic requested.
    
    :param z1: Tuple (a, b) where complex number is a + bi
    :param z2: Tuple (c, d) where complex number is c + di
    :return: Integer indicating relationship between magnitudes (-1, 0, or 1)
    """
    
    # Calculate squared magnitude of z1 = a^2 + b^2
    mag_sq_1 = z1[0] * z1[0] + z1[1] * z1[1]
    
    # Calculate squared magnitude of z2 = c^2 + d^2
    mag_sq_2 = z2[0] * z2[0] + z2[1] * z2[1]
    
    if mag_sq_1 < mag_sq_2:
        return -1
    elif mag_sq_1 > mag_sq_2:
        return 1
    else:
        return 0

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input)
    
    # Sample Complex Numbers
    z1 = (3.0, 4.0)          # |z1| = sqrt(9 + 16) = 5
    z2 = (1.0, 7.0)          # |z2| = sqrt(1 + 49) ≈ 7.07
    
    result = compare_magnitudes(z1, z2)
    
    print(f"Comparing magnitudes of {z1} and {z2}")
    if result == -1:
        print("Magnitude of first number is smaller.")
    elif result == 1:
        print("Magnitude of second number is larger (First magnitude > Second).") # Note logic correction in output message
    else:
        print("Magnitudes are equal.")
    
    # Corrected Logic Explanation for Output based on return value mapping above:
    if compare_magnitudes(z1, z2) == -1:
        msg = "Magnitude of first number is smaller."
    elif compare_magnitudes(z1, z2) == 1:
        msg = "Magnitude of first number is larger than the second." # Fixed text to match return code logic (if z1 > z2 returns 1)
        
        print(f"Result ({msg})")