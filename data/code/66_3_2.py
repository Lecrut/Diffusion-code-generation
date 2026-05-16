import sys
def check_non_decreasing(line):
    try:
        numbers = list(map(int, line.split()))
    except ValueError:
        return False
    if len(numbers) < 2:
        return True
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i+1]:
            return False
    return True
if __name__ == '__main__':
    sample_input_1 = "1 3 5 7"
    sample_input_2 = "1 5 3 7"
    sample_input_3 = "10 20 20 30"
    sample_input_4 = "5 5 5"
    sample_input_5 = "1 2 1"
    sample_input_6 = "10"
    test_cases = [
        (sample_input_1, True),
        (sample_input_2, False),
        (sample_input_3, True),
        (sample_input_4, True),
        (sample_input_5, False),
        (sample_input_6, True)
    ]
    for input_line, expected in test_cases:
        result = check_non_decreasing(input_line)
        assert result == expected, f"Input: '{input_line}', Expected: {expected}, Got: {result}"
        print(f"Input: '{input_line}' -> Result: {result} (Pass)")