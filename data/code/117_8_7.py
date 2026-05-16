def calculate_difference(amount1, amount2):
    if not isinstance(amount1, (int, float)) or not isinstance(amount2, (int, float)):
        raise ValueError("Both inputs must be numeric types.")
    return amount1 - amount2
if __name__ == '__main__':
    try:
        result1 = calculate_difference(10.5, 5.2)
        print(f"Difference between 10.5 and 5.2 is: {result1}")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        calculate_difference("a", 5)
    except ValueError as e:
        print(f"Error: {e}")
    try:
        calculate_difference(10, [5])
    except ValueError as e:
        print(f"Error: {e}")