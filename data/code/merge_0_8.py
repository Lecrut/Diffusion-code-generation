def safe_add(a, b):
    try:
        result = a + b
        return result
    except TypeError:
        raise ValueError("Inputs must be numeric for addition")
if __name__ == '__main__':
    print(safe_add(5, 3))
    try:
        safe_add(5, "3")
    except ValueError as e:
        print(f"Error caught: {e}")
    try:
        safe_add("5", 3)
    except ValueError as e:
        print(f"Error caught: {e}")