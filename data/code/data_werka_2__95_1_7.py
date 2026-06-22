def combine_checks(a, b, c):
    if a <= 0:
        return False
    if b % 2 != 0:
        return False
    if c % a != 0:
        return False
    return True

if __name__ == '__main__':
    result = combine_checks(2, 4, 8)
    print(result)