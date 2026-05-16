import sys
def check_strictly_increasing(input_line):
    try:
        numbers = list(map(int, input_line.split()))
    except ValueError:
        return "Error: Input contains non-integer values."
    if len(numbers) < 2:
        return "Sequence is too short to compare adjacent pairs."
    for i in range(len(numbers) - 1):
        if numbers[i] >= numbers[i+1]:
            return False
    return True
if __name__ == '__main__':
    sample_input = "1 3 5 7 9"
    result = check_strictly_increasing(sample_input)
    print(result)
    sample_input_decreasing = "1 3 2 5"
    result = check_strictly_increasing(sample_input_decreasing)
    print(result)
    sample_input_error = "1 3 a 5"
    result = check_strictly_increasing(sample_input_error)
    print(result)
    sample_input_equal = "1 3 3 5"
    result = check_strictly_increasing(sample_input_equal)
    print(result)