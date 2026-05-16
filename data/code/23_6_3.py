import math
if __name__ == '__main__':
    a = 3.0
    b = 4.0
    c = 5.0
    d = 12.0
    mag_sq_1 = a**2 + b**2
    mag_sq_2 = c**2 + d**2
    if mag_sq_1 > mag_sq_2:
        print("Magnitude of z1 is greater than the magnitude of z2")
    elif mag_sq_1 < mag_sq_2:
        print("Magnitude of z1 is less than the magnitude of z2")
    else:
        print("Magnitudes of z1 and z2 are equal")