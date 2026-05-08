def calculate_three_sum(a, b, c):
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise ValueError("All inputs must be numerical.")
    return a + b + c
if __name__ == '__main__':
    print(calculate_three_sum(1, 2, 3))
    print(calculate_three_sum(10, 20, 30))
    try:
        calculate_three_sum(1, 2, "a")
    except ValueError as e:
        print(f"Error caught: {e}")
    try:
        calculate_three_sum(1.5, 2.5, 3.0)
    except ValueError as e:
        print(f"Error caught: {e}")