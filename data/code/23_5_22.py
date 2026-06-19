import math

def compare_magnitude(z1, z2):
    a, b = z1
    c, d = z2
    mag1_squared = a**2 + b**2
    mag2_squared = c**2 + d**2
    return mag1_squared > mag2_squared

if __name__ == '__main__':
    z1 = (3, 4)
    z2 = (5, 12)
    result = compare_magnitude(z1, z2)
    print(result)