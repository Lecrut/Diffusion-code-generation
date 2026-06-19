def compare_large_integers(num1, num2):
    if num1 > num2:
        return 'num1 is greater'
    elif num1 < num2:
        return 'num2 is greater'
    else:
        return 'both are equal'
if __name__ == '__main__':
    large_num1 = 9876543210987654321098765432109876543210
    large_num2 = 1234567890123456789012345678901234567890
    result = compare_large_integers(large_num1, large_num2)
    print(result)