def compare_numbers(num1, num2):
    return num1 if num1 > num2 else num2

if __name__ == '__main__':
    number_a = 12345678901234567890
    number_b = 98765432109876543210
    larger_number = compare_numbers(number_a, number_b)
    print(f"Number A: {number_a}")
    print(f"Number B: {number_b}")
    print(f"The larger number is: {larger_number}")