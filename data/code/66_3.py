import sys
def check_non_decreasing(line):
    try:
        numbers = list(map(int, line.split()))
    except ValueError:
        return False
    if len(numbers) < 2:
        return True
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i-1]:
            return False
    return True
if __name__ == '__main__':
    sample_input = "1 3 5 7 9"
    result = check_non_decreasing(sample_input)
    print(result)
    sample_input_2 = "1 3 2 5"
    result_2 = check_non_decreasing(sample_input_2)
    print(result_2)
    sample_input_3 = "10 20 30"
    result_3 = check_non_decreasing(sample_input_3)
    print(result_3)
    sample_input_4 = "5 5 5"
    result_4 = check_non_decreasing(sample_input_4)
    print(result_4)
    sample_input_5 = "1 5 4"
    result_5 = check_non_decreasing(sample_input_5)
    print(result_5)