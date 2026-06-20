POSITIVE_THRESHOLD = 100

def validate_input(a, b, c):
    return (a & 2 == 0) and a > 0 and a < POSITIVE_THRESHOLD \
           and (b & 2 == 0) and b > 0 and b < POSITIVE_THRESHOLD \
           and (c & 2 == 0) and c > 0 and c < POSITIVE_THRESHOLD

if __name__ == '__main__':
    print(validate_input(10, 20, 30))
    print(validate_input(100, 20, 30))
    print(validate_input(5, 10, 99))
    print(validate_input(10, 21, 30))