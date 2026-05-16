import math
if __name__ == '__main__':
    z1_real = 3.0
    z1_imag = 4.0
    z2_real = 5.0
    z2_imag = 12.0
    mag_sq_z1 = z1_real**2 + z1_imag**2
    mag_sq_z2 = z2_real**2 + z2_imag**2
    if mag_sq_z1 > mag_sq_z2:
        result = "z1 has a larger squared magnitude"
    elif mag_sq_z2 > mag_sq_z1:
        result = "z2 has a larger squared magnitude"
    else:
        result = "The squared magnitudes are equal"
    print(result)