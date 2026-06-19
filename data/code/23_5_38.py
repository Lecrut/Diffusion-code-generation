import math

def compare_complex_magnitudes(a, b, c, d):
    magnitude1_squared = a**2 + b**2
    magnitude2_squared = c**2 + d**2
    if magnitude1_squared > magnitude2_squared:
        return "z1 has a greater magnitude"
    elif magnitude1_squared < magnitude2_squared:
        return "z2 has a greater magnitude"
    else:
        return "Both complex numbers have the same magnitude"

if __name__ == '__main__':
    z1_real = 3
    z1_imag = 4
    z2_real = 5
    z2_imag = 12
    
    result = compare_complex_magnitudes(z1_real, z1_imag, z2_real, z2_imag)
    print(result)