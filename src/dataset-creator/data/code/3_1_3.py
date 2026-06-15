def divide_two_numbers(a, b):
    try:
        result = a / b
        return result
    except TypeError:
        raise ValueError("Both inputs must be numeric.")
    except ZeroDivisionError:
        raise ZeroDivisionError("Cannot divide by zero.")
if __name__ == '__main__':
    print(divide_two_numbers(10.0, 2.5))
    print(divide_two_numbers(15.0, 3.0))
    try:
        divide_two_numbers(10.0, "a")
    except ValueError as e:
        print(f"Error caught: {e}")
    try:
        divide_two_numbers(5.0, 0.0)
    except ZeroDivisionError as e:
        print(f"Error caught: {e}")