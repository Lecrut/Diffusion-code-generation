import math

def compare_magnitude(z1, z2):
    a, b = z1
    c, d = z2
    magnitude_z1_squared = a**2 + b**2
    magnitude_z2_squared = c**2 + d**2
    
    if magnitude_z1_squared > magnitude_z2_squared:
        return "z1 has greater magnitude"
    elif magnitude_z1_squared < magnitude_z2_squared:
        return "z2 has greater magnitude"
    else:
        return "Both have equal magnitude"

if __name__ == '__main__':
    z1 = (3, 4)
    z2 = (5, 12)
    result = compare_magnitude(z1, z2)
    print(result)