def check_consistency(a, b, output):
    expected = a & b
    return output == expected
if __name__ == '__main__':
    print(check_consistency(1, 0, 0))
    print(check_consistency(1, 1, 1))
    print(check_consistency(1, 0, 1))
    print(check_consistency(0, 0, 0))
    print(check_consistency(1, 1, 0))