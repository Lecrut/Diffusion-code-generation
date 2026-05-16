def compare_temperatures(temp1, temp2, tolerance=1):
    difference = abs(temp1 - temp2)
    return difference <= tolerance
if __name__ == '__main__':
    temp_a = 25.5
    temp_b = 26.8
    tolerance_val = 1
    result = compare_temperatures(temp_a, temp_b, tolerance_val)
    print(result)
    temp_c = 30.0
    temp_d = 32.5
    result2 = compare_temperatures(temp_c, temp_d, tolerance_val)
    print(result2)
    temp_e = 15.0
    temp_f = 14.0
    result3 = compare_temperatures(temp_e, temp_f, tolerance_val)
    print(result3)