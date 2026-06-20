def range_check(a, b, c):
    return 20 <= a <= 30 and 15 <= b <= 25 and (10 <= c <= 40)
if __name__ == '__main__':
    print(range_check(25, 20, 30))
    print(range_check(25, 30, 20))