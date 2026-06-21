def find_greatest(a, b, c):
    return a if a >= b and a >= c else (b if b >= a and b >= c else c)

if __name__ == '__main__':
    print(find_greatest(10, 25, 15))
    print(find_greatest(-1, -2, -3))
    print(find_greatest(5, 5, 5))
    print(find_greatest(100, 1, 99))