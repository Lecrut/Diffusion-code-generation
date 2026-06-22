def compare_large_integers(num1, num2):
    if not isinstance(num1, int) or not isinstance(num2, int):
        raise ValueError("Both inputs must be integers.")
    
    if num1 > num2:
        return 'num1 is greater'
    elif num1 < num2:
        return 'num2 is greater'
    else:
        return 'both numbers are equal'

if __name__ == '__main__':
    try:
        number1 = 987654321098765432109876543210
        number2 = 123456789012345678901234567890
        result = compare_large_integers(number1, number2)
        print(result)
    except ValueError as e:
        print(e)