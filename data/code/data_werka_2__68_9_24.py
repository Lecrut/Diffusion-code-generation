def validate_numbers(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Both inputs must be numbers")

def find_difference(num1, num2):
    validate_numbers(num1, num2)
    return abs(num1 - num2)

if __name__ == '__main__':
    sample_values = [
        (10, 4),
        (-5, 15),
        (7.5, 3.2),
        (0, 0),
        (100, 25),
        (-10, -20)
    ]
    
    for num1, num2 in sample_values:
        try:
            result = find_difference(num1, num2)
            print(f"The absolute difference between {num1} and {num2} is: {result}")
        except ValueError as e:
            print(e)