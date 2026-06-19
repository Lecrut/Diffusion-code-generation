import math

def compare_magnitudes(z1, z2):
    mag1 = z1[0]**2 + z1[1]**2
    mag2 = z2[0]**2 + z2[1]**2
    return mag1 > mag2

if __name__ == '__main__':
    z1 = (3, 4)
    z2 = (5, 12)
    result = compare_magnitudes(z1, z2)
    print(result)