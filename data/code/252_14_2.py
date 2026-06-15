def compare_numbers(num1, num2):
    if num1 > num2:
        print(f"The first number ({num1}) is greater than the second number ({num2}).")
    elif num1 < num2:
        print(f"The first number ({num1}) is less than the second number ({num2}).")
    else:
        print(f"The first number ({num1}) is equal to the second number ({num2}).")
if __name__ == '__main__':
    sample_num1 = 42
    sample_num2 = 105
    integer_num1 = int(sample_num1)
    integer_num2 = int(sample_num2)
    print(f"Comparing sample numbers: {integer_num1} and {integer_num2}")
    compare_numbers(integer_num1, integer_num2)