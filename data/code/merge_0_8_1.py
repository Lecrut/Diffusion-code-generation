def safe_addition(a, b):
    try:
        result = a + b
        return result
    except TypeError:
        raise ValueError("Inputs must be numeric for addition")
if __name__ == '__main__':
    print(safe_addition(5, 3))
    try:
        safe_addition(5, "hello")
    except ValueError as e:
        print(f"Error caught: {e}")