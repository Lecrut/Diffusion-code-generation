def validate_input(a, b, c):
    return (a > 0) & (b > 0) & (c > 0) & (a % 2 == 0) & (b % 2 == 0) & (c % 2 == 0) & (a < 100) & (b < 100) & (c < 100)

if __name__ == '__main__':
    print(validate_input(4, 6, 8))