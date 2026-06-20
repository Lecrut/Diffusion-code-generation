def sum_three_floats(a: float, b: float, c: float) -> float:
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise ValueError("All inputs must be numerical.")
    return a + b + c

if __name__ == '__main__':
    try:
        result1 = sum_three_floats(1.5, 2.5, 3.0)
        print(f"Result 1: {result1}")
    except ValueError as e:
        print(f"Error 1: {e}")

    try:
        result2 = sum_three_floats(4.0, 5.5, 6.6)
        print(f"Result 2: {result2}")
    except ValueError as e:
        print(f"Error 2: {e}")

    try:
        sum_three_floats(1, "a", 3)
    except ValueError as e:
        print(f"Error 3: {e}")