def check_conditions(a, b, c):
    return a > 0 and b % 2 == 0 and c < 100

if __name__ == '__main__':
    print(check_conditions(50, 4, 99))