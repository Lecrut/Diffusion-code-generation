def is_valid_integer_list(numbers):
    if not all(isinstance(x, int) for x in numbers):
        return False
    return True

def find_middle_integer(numbers):
    if not numbers:
        return None
    if not is_valid_integer_list(numbers):
        raise ValueError("Input contains non-integer values.")
    n = len(numbers)
    middle_index = n // 2
    if n % 2 == 1:
        return numbers[middle_index]
    else:
        return (numbers[middle_index - 1] + numbers[middle_index]) // 2

if __name__ == '__main__':
    sample_input = [5, 15, 25, 35, 45, 55]
    try:
        middle = find_middle_integer(sample_input)
        print(middle)
    except ValueError as e:
        print(f"Error: {e}")