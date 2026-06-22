def validate_input(*args):
    if not all(isinstance(x, (int, float)) for x in args):
        raise ValueError("All arguments must be integers or floats")
    if len(args) != 7:
        raise ValueError("Exactly seven arguments are required")

def sum_of_seven_integers(*args):
    validate_input(*args)
    return sum(args)

if __name__ == '__main__':
    result1 = sum_of_seven_integers(1, 2, 3, 4, 5, 6, 7)
    print(f"Sum of (1, 2, 3, 4, 5, 6, 7): {result1}")