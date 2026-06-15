def calculate_difference(a, b):
    try:
        return a - b
    except TypeError:
        raise TypeError("Both arguments must be numerical types.")
    except Exception as e:
        raise ValueError(f"An unexpected error occurred: {e}")
if __name__ == '__main__':
    print(calculate_difference(10, 4))
    print(calculate_difference(5.5, 2.3))
    try:
        calculate_difference(10, "error")
    except TypeError as e:
        print(f"Error caught: {e}")
    try:
        calculate_difference("a", 5)
    except TypeError as e:
        print(f"Error caught: {e}")