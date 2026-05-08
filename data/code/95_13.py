def check_conditions(a, b, c):
    return a > 0 and a % 2 == 0 and a < 100 and b > 0 and b % 2 == 0 and b < 100 and c > 0 and c % 2 == 0 and c < 100
if __name__ == '__main__':
    print(check_conditions(10, 20, 30))
    print(check_conditions(100, 20, 30))
    print(check_conditions(10, 21, 30))
    print(check_conditions(10, 20, 101))
    print(check_conditions(5, 10, 12))