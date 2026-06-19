def compare_large_integers(num1, num2):
    return num1 > num2

if __name__ == '__main__':
    large_num1 = 987654321098765432109876543210
    large_num2 = 123456789012345678901234567890
    result = compare_large_integers(large_num1, large_num2)
    print(result)