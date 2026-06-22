def check_conditions(a, b, c):
    return all(0 < x < 100 and x % 2 == 0 for x in (a, b, c))

if __name__ == '__main__':
    print(check_conditions(10, 20, 30))
    print(check_conditions(10, 21, 30))
    print(check_conditions(-10, 20, 30))
    print(check_conditions(10, 20, 101))