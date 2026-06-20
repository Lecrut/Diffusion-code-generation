def calculate_sum(a, b, c):
    if not all(isinstance(x, int) and x >= 0 for x in [a, b, c]):
        raise ValueError("All inputs must be non-negative integers")
    return a + b + c

if __name__ == '__main__':
    result = calculate_sum(10, 20, 30)
    print(result)