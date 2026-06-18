def calculate_difference(a, b):
    try:
        return a - b
    except TypeError:
        raise TypeError("Both arguments must be numerical.")
    except Exception as e:
        raise ValueError(f"An unexpected error occurred: {e}")
if __name__ == '__main__':
    num1 = 25
    num2 = 10
    result1 = calculate_difference(num1, num2)
    print(f"Difference between {num1} and {num2}: {result1}")
    num3 = 5.5
    num4 = 2.5
    result2 = calculate_difference(num3, num4)
    print(f"Difference between {num3} and {num4}: {result2}")
    try:
        calculate_difference(10, "a")
    except TypeError as e:
        print(f"Error caught: {e}")