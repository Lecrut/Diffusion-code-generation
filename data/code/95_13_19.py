def validate_input(a, b, c):
    return all(x > 0 and x % 2 == 0 and x < 100 for x in (a, b, c))

if __name__ == '__main__':
    print(validate_input(2, 4, 6))