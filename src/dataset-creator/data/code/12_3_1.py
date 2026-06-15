def perform_subtraction(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers.")
    return a - b
if __name__ == '__main__':
    print(perform_subtraction(10, 4))
    try:
        perform_subtraction(10.5, 4)
    except TypeError as e:
        print(f"Error caught: {e}")
    try:
        perform_subtraction("a", 4)
    except TypeError as e:
        print(f"Error caught: {e}")