import math

def compare_magnitude_squared(z1_real: float, z1_imag: float, 
                             z2_real: float, z2_imag: float) -> str:
    """
    Compares the squared magnitudes of two complex numbers.
    
    Parameters:
        z1_real (float): Real part of first complex number
        z1_imag (float): Imaginary part of first complex number
        z2_real (float): Real part of second complex number
        z2_imag (float): Imaginary part of second complex number
        
    Returns:
        str: Comparison result ('z1_greater', 'equal', or 'z2_greater')
    """
    # Calculate squared magnitudes directly to avoid square root operations for comparison efficiency
    mag_sq_1 = z1_real ** 2 + z1_imag ** 2
    mag_sq_2 = z2_real ** 2 + z2_imag ** 2
    
    if mag_sq_1 > mag_sq_2:
        return 'z1_greater'
    elif mag_sq_2 > mag_sq_1:
        return 'z2_greater'
    else:
        return 'equal'

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    # Sample complex numbers
    z1_real = 3.0
    z1_imag = 4.0
    z2_real = 5.0
    z2_imag = 12.0
    
    result = compare_magnitude_squared(z1_real, z1_imag, z2_real, z2_imag)
    
    # Optional: Print results for verification (no interactive prompts used)
    print(f"z1 magnitude squared ({z1_real}^2 + {z1_imag}^2): {mag_sq_1}")
    mag_sq_2 = 5.0 ** 2 + 12.0 ** 2
    print(f"z2 magnitude squared ({z2_real}^2 + {z2_imag}^2): {mag_sq_2}")
    
    if result == 'equal':
        # In case of equality, we can optionally compute actual magnitudes using math.sqrt for demonstration
        mag1 = math.sqrt(mag_sq_1)
        mag2 = math.sqrt(mag_sq_2)
        print(f"Actual magnitudes are equal: {mag1} == {mag2}")
    else:
        if result == 'z1_greater':
            print("Result: |z1| > |z2|")
        elif result == 'z2_greater':
            print("Result: |z2| > |z1|")