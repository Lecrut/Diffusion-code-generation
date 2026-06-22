def validate_numbers(num1, num2):
    if not isinstance(num1, int) or not isinstance(num2, int):
        raise ValueError("Both inputs must be integers")
    
def calculate_sum(num1, num2):
    validate_numbers(num1, num2)
    return num1 + num2

if __name__ == '__main__':
    number1 = 15
    number2 = 27
    result = calculate_sum(number1, number2)
    print(result)