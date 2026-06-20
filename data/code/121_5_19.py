def compare_complex_numbers(c1, c2):
    abs_c1 = abs(c1)
    abs_c2 = abs(c2)
    if abs_c1 > abs_c2:
        return f"{c1} has a greater absolute value than {c2}"
    elif abs_c1 < abs_c2:
        return f"{c2} has a greater absolute value than {c1}"
    else:
        return "Both complex numbers have the same absolute value"

if __name__ == '__main__':
    c_a = 3 + 4j
    c_b = -5 + 12j
    result = compare_complex_numbers(c_a, c_b)
    print(result)