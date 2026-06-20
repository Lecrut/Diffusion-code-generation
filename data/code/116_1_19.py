def validate_inputs(a, b, c):
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise ValueError("All inputs must be numerical.")

def calculate_three_sum(a, b, c):
    validate_inputs(a, b, c)
    return a + b + c

if __name__ == '__main__':
    result1 = calculate_three_sum(1.5, 2.5, 3.0)
    print(f"Result 1: {result1}")
    try:
        calculate_three_sum(1, "a", 3)
    except ValueError as e:
        print(f"Error caught: {e}")