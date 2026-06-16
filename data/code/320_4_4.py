def safe_subtract(a, b):
    try:
        num_a = float(a)
        num_b = float(b)
        result = num_a - num_b
        return result
    except (ValueError, TypeError):
        raise ValueError("Both inputs must be valid numeric values.")
if __name__ == '__main__':
    print(safe_subtract(10, 3))
    try:
        safe_subtract("hello", 3)
    except ValueError as e:
        print(f"Error caught: {e}")
    try:
        safe_subtract(5.5, "text")
    except ValueError as e:
        print(f"Error caught: {e}")
    try:
        safe_subtract([1, 2], 4)
    except ValueError as e:
        print(f"Error caught: {e}")