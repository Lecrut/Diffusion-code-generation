import math

def compare_magnitudes(z1_real, z1_imag, z2_real, z2_imag):
    magnitude_z1_squared = z1_real**2 + z1_imag**2
    magnitude_z2_squared = z2_real**2 + z2_imag**2
    
    if magnitude_z1_squared > magnitude_z2_squared:
        return "z1 has a greater magnitude"
    elif magnitude_z1_squared < magnitude_z2_squared:
        return "z2 has a greater magnitude"
    else:
        return "Both complex numbers have the same magnitude"

if __name__ == '__main__':
    z1_real, z1_imag = 3, 4
    z2_real, z2_imag = 5, 12
    
    result = compare_magnitudes(z1_real, z1_imag, z2_real, z2_imag)
    print(result)