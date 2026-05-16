def check_positive(number):
    if number > 0:
        return True
    else:
        return False
if __name__ == '__main__':
    sample_inputs = [10, -5, 0, 3.14, "abc"]
    for input_value in sample_inputs:
        try:
            num = int(input_value)
            result = check_positive(num)
            print(f"Input: {input_value}, Is Positive: {result}")
        except ValueError:
            print(f"Input: {input_value}, Error: Invalid integer input.")