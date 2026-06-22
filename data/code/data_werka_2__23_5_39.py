import math

def compare_complex_magnitude(z1, z2):
    magnitude_z1 = z1[0] ** 2 + z1[1] ** 2
    magnitude_z2 = z2[0] ** 2 + z2[1] ** 2
    if magnitude_z1 > magnitude_z2:
        return 1
    elif magnitude_z1 < magnitude_z2:
        return -1
    else:
        return 0
if __name__ == '__main__':
    z1 = (3, 4)
    z2 = (5, 12)
    result = compare_complex_magnitude(z1, z2)
    print(result)