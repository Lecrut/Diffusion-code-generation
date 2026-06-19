import math

def compare_magnitude(z1, z2):
    magnitude_z1 = z1[0]**2 + z1[1]**2
    magnitude_z2 = z2[0]**2 + z2[1]**2
    
    if magnitude_z1 > magnitude_z2:
        return "z1 is greater"
    elif magnitude_z1 < magnitude_z2:
        return "z2 is greater"
    else:
        return "both are equal"

if __name__ == '__main__':
    z1 = (3, 4)
    z2 = (5, 12)
    result = compare_magnitude(z1, z2)
    print(result)