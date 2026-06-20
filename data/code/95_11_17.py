def check_conditions(a, b, c):
    return all([a > 0, a % 2 == 0, a < 100])

if __name__ == '__main__':
    print(check_conditions(42, 78, 56))
    print(check_conditions(33, 90, 120))