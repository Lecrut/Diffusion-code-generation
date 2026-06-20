MAX_VALUE = 100

def check_conditions(a, b, c):
    return a > 0 and b > 0 and (c > 0) and (a % 2 == 0) and (b % 2 == 0) and (c % 2 == 0) and (a < MAX_VALUE) and (b < MAX_VALUE) and (c < MAX_VALUE)
if __name__ == '__main__':
    print(check_conditions(4, 6, 8))
    print(check_conditions(-2, 4, 10))
    print(check_conditions(3, 5, 97))
    print(check_conditions(2, 4, 99))