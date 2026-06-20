def calculate_difference(a, b):
    return abs(a - b)

if __name__ == '__main__':
    num1 = 123456789012345678901234567890
    num2 = 987654321098765432109876543210
    result = calculate_difference(num1, num2)
    print(f"The absolute difference between {num1} and {num2} is: {result}")