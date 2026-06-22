def find_largest(a, b, c):
    if not all(isinstance(x, (int, float)) for x in (a, b, c)):
        raise TypeError("All arguments must be numeric")
    return a if a > b else b if b > c else c

if __name__ == '__main__':
    print(find_largest(10, 25, 15))