def compare_numbers(a, b):
    diff = a - b
    sign_bit = (diff >> 31) & 1
    return sign_bit == 0

if __name__ == '__main__':
    num1 = 10
    num2 = 5
    result1 = compare_numbers(num1, num2)
    print(f"Comparing {num1} and {num2}: {'greater' if result1 else 'less'}")

    num3 = 7
    num4 = 7
    result2 = compare_numbers(num3, num4)
    print(f"Comparing {num3} and {num4}: {'equal' if result2 else 'not equal'}")