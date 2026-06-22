def validate_input(a, b, c):
    def check(n):
        return n > 0 and n < 100 and (n & 1) == 0
    return check(a) and check(b) and check(c)

if __name__ == '__main__':
    print(validate_input(2, 4, 6))
    print(validate_input(0, 2, 4))
    print(validate_input(2, 3, 4))
    print(validate_input(2, 4, 100))