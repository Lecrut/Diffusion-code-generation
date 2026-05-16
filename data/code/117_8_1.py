def calculate_difference(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Inputs must be numeric types")
    return a - b
if __name__ == '__main__':
    try:
        result1 = calculate_difference(10, 5)
        print(f"Difference between 10 and 5: {result1}")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        result2 = calculate_difference("a", 5)
    except ValueError as e:
        print(f"Error: {e}")
    try:
        result3 = calculate_difference(3.5, "2")
    except ValueError as e:
        print(f"Error: {e}")