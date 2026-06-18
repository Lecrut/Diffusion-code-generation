def perform_subtraction(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Inputs must be integers")
    return a - b
if __name__ == '__main__':
    print(perform_subtraction(10, 3))
    try:
        perform_subtraction(10.5, 3)
    except TypeError as e:
        print(f"Error caught: {e}")
    try:
        perform_subtraction("a", 3)
    except TypeError as e:
        print(f"Error caught: {e}")