def check_values(a, b, c):
    return (a > 0, b % 2 == 0, c % a == 0)

if __name__ == '__main__':
    print(check_values(5, 4, 10))