def sum_of_six_numbers(a, b, c, d, e, f):
    if not all(isinstance(x, (int, float)) for x in [a, b, c, d, e, f]):
        raise ValueError("All arguments must be numbers.")
    return a + b + c + d + e + f

def validate_numbers(*args):
    if len(args) != 6:
        raise ValueError("Exactly six numbers are required.")
    for num in args:
        if not isinstance(num, (int, float)):
            raise ValueError("All arguments must be numbers.")

if __name__ == '__main__':
    validate_numbers(1.5, 2.3, 3, 4.7, 5, 6)
    result = sum_of_six_numbers(1.5, 2.3, 3, 4.7, 5, 6)
    print(result)