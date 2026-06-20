def check_conditions(a, b, c):
    return all(isinstance(x, int) and x > 0 and x % 2 == 0 and x < 100 for x in (a, b, c))

if __name__ == '__main__':
    print(check_conditions(4, 6, 8))
    print(check_conditions(100, 2, 3))