def check_zero_after_evaluation(input_string):
    try:
        number = float(input_string)
        if number == 0:
            return True
        else:
            return False
    except ValueError:
        return False
if __name__ == '__main__':
    test_values = [
        "0",
        "0.0",
        "123",
        "-5",
        "abc",
        "3.14"
    ]
    for value in test_values:
        result = check_zero_after_evaluation(value)
        print(f"Input: '{value}', Result: {result}")