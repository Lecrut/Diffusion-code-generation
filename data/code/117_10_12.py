def validate_numbers(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Both inputs must be numeric.")

def calculate_difference(num1, num2):
    return round(num1 - num2, 4)

if __name__ == '__main__':
    try:
        validate_numbers(15, 7)
        difference = calculate_difference(15, 7)
        print(difference)
    except ValueError as e:
        print(f"Error: {e}")