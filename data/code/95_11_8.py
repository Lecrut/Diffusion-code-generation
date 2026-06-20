def check_conditions(a, b, c):
    return all([a > 0, a % 2 == 0, a < 100, b > 0, b % 2 == 0, b < 100, c > 0, c % 2 == 0, c < 100])

if __name__ == '__main__':
    print(check_conditions(4, 6, 8))