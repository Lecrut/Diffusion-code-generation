calculate_difference = lambda a, b: abs(a - b)

if __name__ == '__main__':
    num1 = 10
    num2 = -5
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        result1 = calculate_difference(num1, num2)
        print(f"Difference between {num1} and {num2}: {result1}")
    else:
        print("Invalid input: Both numbers must be integers or floats.")

    num3 = -15
    num4 = 7
    if isinstance(num3, (int, float)) and isinstance(num4, (int, float)):
        result2 = calculate_difference(num3, num4)
        print(f"Difference between {num3} and {num4}: {result2}")
    else:
        print("Invalid input: Both numbers must be integers or floats.")

    num5 = -100
    num6 = -50
    if isinstance(num5, (int, float)) and isinstance(num6, (int, float)):
        result3 = calculate_difference(num5, num6)
        print(f"Difference between {num5} and {num6}: {result3}")
    else:
        print("Invalid input: Both numbers must be integers or floats.")