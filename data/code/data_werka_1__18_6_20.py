def compare_large_integers(num1, num2):
    if num1 > num2:
        return 'num1 is greater'
    elif num1 < num2:
        return 'num2 is greater'
    else:
        return 'both numbers are equal'
if __name__ == '__main__':
    number1 = 987654321098765432109876543210
    number2 = 123456789012345678901234567890
    result = compare_large_integers(number1, number2)
    print(result)