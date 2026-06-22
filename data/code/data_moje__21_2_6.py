def find_largest(a, b, c):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError("All arguments must be numeric")
    return a if a > b and a > c else b if b > c else c

if __name__ == '__main__':
    print(find_largest(10, 20, 15))