def check_conditions(a, b, c):
    return all(0 < x < 100 and x % 2 == 0 for x in (a, b, c))

if __name__ == '__main__':
    print(check_conditions(2, 4, 6))
    print(check_conditions(2, 4, 102))
    print(check_conditions(2, 3, 4))
    print(check_conditions(-2, 4, 6))