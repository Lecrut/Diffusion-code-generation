import math

def compare_magnitude(z1, z2):
    a, b = z1
    c, d = z2
    mag_z1_squared = a**2 + b**2
    mag_z2_squared = c**2 + d**2
    
    if mag_z1_squared > mag_z2_squared:
        return "z1 is greater"
    elif mag_z1_squared < mag_z2_squared:
        return "z2 is greater"
    else:
        return "Both are equal"

if __name__ == '__main__':
    z1 = (3, 4)
    z2 = (5, 12)
    result = compare_magnitude(z1, z2)
    print(result)