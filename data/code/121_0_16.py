def compare_numbers(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Both inputs must be numbers")
    return max(num1, num2)

if __name__ == '__main__':
    number_a = 1234567890
    number_b = 9876543210
    larger_number = compare_numbers(number_a, number_b)
    print(f"Number A: {number_a}, Number B: {number_b}")
    print(f"The larger number is: {larger_number}")