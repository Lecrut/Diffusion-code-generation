def sum_of_six_numbers(a, b, c, d, e, f):
    if not all(isinstance(x, (int, float)) for x in [a, b, c, d, e, f]):
        raise ValueError("All arguments must be numbers.")
    return a + b + c + d + e + f

if __name__ == '__main__':
    result = sum_of_six_numbers(10, 20, 30, 40, 50, 60)
    print(result)