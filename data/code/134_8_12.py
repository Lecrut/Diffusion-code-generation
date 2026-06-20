def count_and_check_exclusive(a, b, c, d, e):
    return (a + b + c + d + e) == 1

if __name__ == '__main__':
    result = count_and_check_exclusive(True, False, False, False, False)
    print(result)