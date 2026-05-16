import sys
def check_strictly_increasing(input_line):
    try:
        numbers = list(map(int, input_line.split()))
    except ValueError:
        return False
    except Exception:
        return False
    if len(numbers) < 2:
        return True
    for i in range(len(numbers) - 1):
        if numbers[i] >= numbers[i+1]:
            return False
    return True
if __name__ == '__main__':
    sample_input = "1 3 5 7 9"
    result = check_strictly_increasing(sample_input)
    print(result)
    sample_input_fail = "1 3 2 7 9"
    result_fail = check_strictly_increasing(sample_input_fail)
    print(result_fail)
    sample_input_error = "1 3 a 5"
    result_error = check_strictly_increasing(sample_input_error)
    print(result_error)
    sample_input_equal = "1 1 2 3"
    result_equal = check_strictly_increasing(sample_input_equal)
    print(result_equal)