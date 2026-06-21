def find_largest(a, b, c):
    if not all(isinstance(x, (int, float)) for x in (a, b, c)):
        raise TypeError("All arguments must be numeric")
    return a if a > b and a > c else (b if b > a and b > c else c)

if __name__ == '__main__':
    result = find_largest(10, 25, 15)
    print(result)