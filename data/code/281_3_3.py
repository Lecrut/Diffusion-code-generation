def sum_of_six_numbers(a, b, c, d, e, f):
    if not all(isinstance(x, (int, float)) for x in [a, b, c, d, e, f]):
        raise ValueError("All arguments must be numbers.")
    return a + b + c + d + e + f

if __name__ == '__main__':
    result = sum_of_six_numbers(1.5, 2.3, 3, 4.7, 5, 6)
    print(result)