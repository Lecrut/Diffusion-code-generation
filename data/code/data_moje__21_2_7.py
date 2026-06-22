def max_of_three(a, b, c):
    if not all(isinstance(x, (int, float)) for x in (a, b, c)):
        raise TypeError("All arguments must be numeric")
    return a if (a >= b and a >= c) else (b if b >= c else c)

if __name__ == '__main__':
    result = max_of_three(10, 20, 5)
    print(result)