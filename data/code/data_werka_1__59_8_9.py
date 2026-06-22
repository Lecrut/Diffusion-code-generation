def find_middle_item(numbers):
    def is_valid_list(input_list):
        return isinstance(input_list, list) and all(isinstance(x, (int, float)) for x in input_list)

    if not is_valid_list(numbers):
        raise ValueError("Input must be a list of numbers")

    length = len(numbers)
    if length == 0:
        raise ValueError("List cannot be empty")

    middle_index = (length - 1) // 2
    return numbers[middle_index]

if __name__ == '__main__':
    sample_values_odd = [1, 3, 5, 7, 9]
    sample_values_even = [2, 4, 6, 8, 10, 12]

    print("Middle element of the odd-length list:", find_middle_item(sample_values_odd))
    print("Middle element of the even-length list:", find_middle_item(sample_values_even))