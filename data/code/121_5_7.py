def compare_complex_numbers(c1, c2):
    return abs(c1) > abs(c2)

if __name__ == '__main__':
    result = compare_complex_numbers(3 + 4j, 1 + 1j)
    print(result)