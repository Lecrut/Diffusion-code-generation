def calculate_difference(num1, num2):
    return num1 - num2
if __name__ == '__main__':
    num1 = 15
    num2 = 7
    try:
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            raise ValueError("Input must be numeric.")
        difference = calculate_difference(num1, num2)
        print(difference)
    except ValueError as e:
        print(f"Error: {e}")
    except TypeError:
        print("Error: One or both inputs were not valid numbers.")