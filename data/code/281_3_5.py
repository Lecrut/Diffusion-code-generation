def validate_numbers(*args):
    if len(args) != 6:
        raise ValueError("Exactly six numbers are required.")
    if not all(isinstance(x, (int, float)) for x in args):
        raise ValueError("All arguments must be numbers.")

def sum_of_six_numbers(a, b, c, d, e, f):
    validate_numbers(a, b, c, d, e, f)
    return a + b + c + d + e + f

if __name__ == '__main__':
    result = sum_of_six_numbers(1.5, 2.3, 3, 4.7, 5, 6)
    print(result)