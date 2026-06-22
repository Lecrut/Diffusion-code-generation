import math

def compare_magnitude_squared(z1, z2):
    mag_sq_z1 = z1[0]**2 + z1[1]**2
    mag_sq_z2 = z2[0]**2 + z2[1]**2
    return mag_sq_z1 > mag_sq_z2

if __name__ == '__main__':
    z1 = (3, 4)
    z2 = (5, 12)
    result = compare_magnitude_squared(z1, z2)
    print(result)