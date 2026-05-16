import sys
def check_strictly_increasing(line):
    try:
        numbers = list(map(int, line.split()))
    except ValueError:
        return False, "Error: Input contains non-integer values."
    if len(numbers) < 2:
        return True, "Sequence is strictly increasing (trivially)."
    for i in range(len(numbers) - 1):
        if numbers[i] >= numbers[i+1]:
            return False, "Sequence is not strictly increasing (found non-increasing pair)."
    return True, "Sequence is strictly increasing."
if __name__ == '__main__':
    sample_input_1 = "1 3 5 7 9"
    sample_input_2 = "1 3 2 7"
    sample_input_3 = "10 5 20"
    sample_input_4 = "1 2 2 3"
    sample_input_5 = "a 1 3"
    sample_input_6 = "10"
    test_cases = [
        (sample_input_1, "Strictly Increasing"),
        (sample_input_2, "Not Strictly Increasing"),
        (sample_input_3, "Not Strictly Increasing"),
        (sample_input_4, "Not Strictly Increasing"),
        (sample_input_5, "Error"),
        (sample_input_6, "Strictly Increasing (Trivially)")
    ]
    for input_line, expected_result in test_cases:
        is_increasing, message = check_strictly_increasing(input_line)
        status = "PASS" if (is_increasing == (expected_result == "Strictly Increasing" or expected_result == "Not Strictly Increasing" or expected_result == "Error")) else "FAIL"
        print(f"Input: '{input_line}'")
        print(f"Result: {is_increasing}, Message: {message} (Expected: {expected_result}) - {status}\n")