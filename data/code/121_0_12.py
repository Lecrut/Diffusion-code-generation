def compare_numbers(a, b):
    return a if a > b else b

if __name__ == '__main__':
    num1 = 123456789012345678901234567890
    num2 = 987654321098765432109876543210
    larger_num = compare_numbers(num1, num2)
    print(f"The larger number is: {larger_num}")