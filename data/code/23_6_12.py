import math

def compare_complex_magnitudes(a: float, b: float, c: float, d: float) -> str:
    """
    Compare the magnitudes of two complex numbers z1 = a + bi and z2 = c + di
    by comparing their squared magnitudes. This avoids costly square root operations.

    Returns:
        'z1_larger': if |z1| > |z2|
        'z2_larger': if |z2| > |z1|
        'equal':      if |z1| == |z2| (within floating point tolerance)
    """
    sq_mag_z1 = a * a + b * b
    sq_mag_z2 = c * c + d * d

    # Use a small epsilon for float comparison to handle precision issues
    EPSILON = 1e-9
    
    if abs(sq_mag_z1 - sq_mag_z2) < EPSILON:
        return 'equal'
    
    if sq_mag_z1 > sq_mag_z2 + EPSILON:
        # Optional: calculate actual magnitudes for verification or display if needed.
        mag_z1 = math.sqrt(sq_mag_z1)
        mag_z2 = math.sqrt(sq_mag_z2)
        
        return f'z1_larger (|{mag_z1:.6f}| > |{mag_z2:.6f}|)'

    else:
        # Optional: calculate actual magnitudes for verification or display if needed.
        mag_z1 = math.sqrt(sq_mag_z1)
        mag_z2 = math.sqrt(sq_mag_z2)
        
        return f'z2_larger (|{mag_z2:.6f}| > |{mag_z1:.6f}|)'

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or files.
    
    # Sample 1: z1 = 3 + 4i, z2 = 5 + 0i
    a, b = 3.0, 4.0
    c, d = 5.0, 0.0
    
    print("Comparing z1 =", f"{a}+{b}i", "and z2 =", f"{c}+{d}i")
    
    result = compare_complex_magnitudes(a, b, c, d)
    print(result)

    # Sample 2: Equal magnitudes |3 + 4i| vs |-5 - i*12| -> both are sqrt(25)=5 and sqrt(169+144 no wait) 
    # Let's use a known equal case: z1 = (0, 1), z2 = (-sqrt(2)/2, ... complicated).
    # Simpler integer example for equality check logic: |3^2 + 4^2| = 25. Is there another? Yes, |-5 + 0i|. 
    # Already tested in Sample 1 but let's test strict inequality case and near equal.

    a2, b2 = -3.0, 4.0
    c2, d2 = 3.0, -4.0
    
    print("\nComparing z1 =", f"{a2}+{b2}i", "and z2 =", f"{c2}+{d2}i")
    
    result2 = compare_complex_magnitudes(a2, b2, c2, d2)
    print(result2)

    # Test near equality to trigger epsilon logic if inputs were slightly perturbed (simulated here conceptually).