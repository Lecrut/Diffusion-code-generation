def validate_numbers(a, b, c):
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise ValueError("All inputs must be numerical.")

def calculate_three_sum(a, b, c):
    validate_numbers(a, b, c)
    return a + b + c

if __name__ == '__main__':
    try:
        result1 = calculate_three_sum(1, 2, 3)
        print(f"Result 1: {result1}")
    except ValueError as e:
        print(f"Error 1: {e}")

    try:
        result2 = calculate_three_sum(1.5, 2.5, 3.0)
        print(f"Result 2: {result2}")
    except ValueError as e:
        print(f"Error 2: {e}")

    try:
        calculate_three_sum(1, "a", 3)
    except ValueError as e:
        print(f"Error 3: {e}")