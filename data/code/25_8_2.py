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
    test_cases = [
        "0",
        "0.0",
        "abc",
        "123",
        "-5.5",
        "0.0000000000000001"
    ]
    for test in test_cases:
        result = check_zero_after_evaluation(test)
        print(f"Input: '{test}', Result: {result}")