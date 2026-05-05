import sys
def check_strictly_increasing(line):
    try:
        numbers = list(map(int, line.split()))
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
    sample_input_decreasing = "1 3 2 5"
    result_decreasing = check_strictly_increasing(sample_input_decreasing)
    print(result_decreasing)
    sample_input_non_integer = "1 3 a 5"
    result_non_integer = check_strictly_increasing(sample_input_non_integer)
    print(result_non_integer)
    sample_input_equal = "1 1 2"
    result_equal = check_strictly_increasing(sample_input_equal)
    print(result_equal)