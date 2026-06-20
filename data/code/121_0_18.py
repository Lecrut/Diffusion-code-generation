def validate_numbers(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Both inputs must be numbers")

def compare_magnitude(num1, num2):
    validate_numbers(num1, num2)
    return num1 if num1 > num2 else num2

if __name__ == '__main__':
    number_a = 150
    number_b = 234.5
    larger_number = compare_magnitude(number_a, number_b)
    print(f"The larger number is: {larger_number}")