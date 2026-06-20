def compare_complex_numbers(c1, c2):
    abs_c1 = abs(c1)
    abs_c2 = abs(c2)
    if abs_c1 > abs_c2:
        return 1
    elif abs_c1 < abs_c2:
        return -1
    else:
        return 0

if __name__ == '__main__':
    complex_a = 3 + 4j
    complex_b = 5 + 12j
    result = compare_complex_numbers(complex_a, complex_b)
    print(f"Comparison of {complex_a} and {complex_b}: {result}")