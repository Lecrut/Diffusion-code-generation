import math

def compare_magnitude_squared(z1_real, z1_imag, z2_real, z2_imag):
    magnitude_squared_z1 = z1_real**2 + z1_imag**2
    magnitude_squared_z2 = z2_real**2 + z2_imag**2
    
    if magnitude_squared_z1 > magnitude_squared_z2:
        return "z1 has a greater magnitude"
    elif magnitude_squared_z1 < magnitude_squared_z2:
        return "z2 has a greater magnitude"
    else:
        return "Both complex numbers have the same magnitude"

if __name__ == '__main__':
    z1_real, z1_imag = 3, 4
    z2_real, z2_imag = 5, 12
    
    result = compare_magnitude_squared(z1_real, z1_imag, z2_real, z2_imag)
    print(result)