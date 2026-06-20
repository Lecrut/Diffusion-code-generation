def compare_complex_abs(c1, c2):
    return abs(c1) > abs(c2)

if __name__ == '__main__':
    z1 = 3 + 4j
    z2 = 5 - 12j
    result = compare_complex_abs(z1, z2)
    print(result)