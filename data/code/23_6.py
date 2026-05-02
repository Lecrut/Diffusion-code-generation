import math
if __name__ == '__main__':
    a = 3.0
    b = 4.0
    c = 5.0
    d = 12.0
    mag_sq_1 = a**2 + b**2
    mag_sq_2 = c**2 + d**2
    if mag_sq_1 > mag_sq_2:
        print("Magnitude of z1 is greater.")
    elif mag_sq_1 < mag_sq_2:
        print("Magnitude of z2 is greater.")
    else:
        print("Magnitudes are equal.")