def compare_complex_numbers(z1, z2):
    abs_z1 = abs(z1)
    abs_z2 = abs(z2)
    
    if abs_z1 > abs_z2:
        return f"{z1} has a larger absolute value than {z2}"
    elif abs_z1 < abs_z2:
        return f"{z1} has a smaller absolute value than {z2}"
    else:
        return f"{z1} and {z2} have the same absolute value"

if __name__ == '__main__':
    z1 = 3 + 4j
    z2 = 1 - 1j
    print(compare_complex_numbers(z1, z2))