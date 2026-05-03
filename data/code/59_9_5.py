def find_middle_integer(numbers):
    if not numbers:
        return None
    n = len(numbers)
    if n % 2 == 1:
        middle_index = n // 2
        return numbers[middle_index]
    else:
        middle_right_index = n // 2
        middle_left_index = middle_right_index - 1
        return (numbers[middle_left_index] + numbers[middle_right_index]) // 2
if __name__ == '__main__':
    sample_input = ["1", "5", "3", "9", "2"]
    integer_list = []
    is_valid = True
    for item in sample_input:
        try:
            integer_list.append(int(item))
        except ValueError:
            is_valid = False
            break
    if is_valid:
        result = find_middle_integer(integer_list)
        print(result)
    else:
        print("Error: Input contained non-integer values.")