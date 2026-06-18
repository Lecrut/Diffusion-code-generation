import math

def compare_complex_magnitude(z1_real: float, z1_imag: float, z2_real: float, z2_imag: float) -> int:
    """
    Compare squared magnitudes of two complex numbers to determine which is larger.
    
    Args:
        z1_real (float): Real part of the first complex number (a + bi).
        z1_imag (float): Imaginary part of the first complex number.
        z2_real (float): Real part of the second complex number (c + di).
        z2_imag (float): Imaginary part of the second complex number.
    
    Returns:
        int: 
            1 if |z1| > |z2|,
             -1 if |z1| < |z2|,
              0 otherwise.
    """
    # Compare squared magnitudes directly to avoid computationally expensive square root operations
    sq_mag_1 = z1_real ** 2 + z1_imag ** 2
    sq_mag_2 = z2_real ** 2 + z2_imag ** 2
    
    if sq_mag_1 > sq_mag_2:
        return 1
    elif sq_mag_1 < sq_mag_2:
        return -1
    else:
        return 0

if __name__ == '__main__':
    # Sample values for z1 = a + bi and z2 = c + di
    # z1 is explicitly defined as the larger magnitude in this sample.
    
    # Define complex numbers directly using components to avoid unnecessary sqrt calls during setup comparison logic if needed, 
    # though we only compare here anyway.
    real_part_1: float = 5.0
    imag_part_1: float = 2.0
    
    real_part_2: float = -3.0
    imag_part_2: float = 4.0
    
    # Compute and output comparison result based on squared magnitudes |z|^2 = a^2 + b^2
    sq_mag_z1 = math.sqrt(real_part_1 ** 2) * math.sqrt(imag_part_1 ** 2) if real_part_1 or imag_part_1 else 0 
    # Actually, for the result we just need relative magnitude comparison. The prompt says "compare their squared magnitudes".
    
    res = compare_complex_magnitude(real_part_1, imag_part_1, real_part_2, imag_part_2)
    
    print(f"Comparison Result between z={real_part_1} + {imag_part_1}i and z={real_part_2} + {imag_part_2}i:")
    if res == 1:
        print("|z1| > |z2|")
    elif res == -1:
        print("|z1| < |z2|")
    else:
        print("|z1| = |z2|")