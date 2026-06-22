def find_largest(a, b, c):
    return max(a, b, c)

if __name__ == '__main__':
    print(find_largest(1, 2, 3))
    print(find_largest(9, 7, 5))
    print(find_largest(0, 0, 0))
    print(find_largest(-1, -2, -3))
    print(find_largest(100, 200, 50))