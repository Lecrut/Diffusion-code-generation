def calculate_difference(a, b):
    try:
        result = float(a) - float(b)
        return result
    except (TypeError, ValueError):
        raise TypeError("Both inputs must be convertible to floating-point numbers.")
if __name__ == '__main__':
    print(calculate_difference(10.5, 3.2))
    try:
        calculate_difference("hello", 5.0)
    except TypeError as e:
        print(f"Error caught: {e}")
    try:
        calculate_difference(10, "world")
    except TypeError as e:
        print(f"Error caught: {e}")