import math

def compare_magnitude(z1, z2):
    a, b = z1
    c, d = z2
    magnitude_z1 = a**2 + b**2
    magnitude_z2 = c**2 + d**2
    return magnitude_z1 > magnitude_z2

if __name__ == '__main__':
    z1 = (3, 4)
    z2 = (5, 12)
    result = compare_magnitude(z1, z2)
    print(result)