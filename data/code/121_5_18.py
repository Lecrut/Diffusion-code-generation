def compare_complex_numbers(c1, c2):
    return abs(c1) > abs(c2)

if __name__ == '__main__':
    num1 = 3 + 4j
    num2 = 1 - 1j
    print(compare_complex_numbers(num1, num2))