def logical_combinations(a, b, c):
    return (a and b) or c

if __name__ == '__main__':
    print(logical_combinations(True, False, True))
    print(logical_combinations(False, True, False))
    print(logical_combinations(True, True, False))