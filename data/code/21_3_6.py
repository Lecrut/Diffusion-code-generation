def get_largest(a, b, c):
    return a if a > b and a > c else (b if b > c else c)

if __name__ == '__main__':
    result = get_largest(3.14, 2.71, 1.61)
    print(result)