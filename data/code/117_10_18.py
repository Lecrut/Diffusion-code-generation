def calculate_difference(num1, num2):
    return round(num1 - num2, 4)

if __name__ == '__main__':
    try:
        num1 = 15.3456789
        num2 = 7.1234567
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            raise ValueError("Inputs must be numeric.")
        difference = calculate_difference(num1, num2)
        print(difference)
    except ValueError as e:
        print(f"Error: {e}")