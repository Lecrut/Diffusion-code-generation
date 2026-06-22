def get_middle_element(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    length = len(numbers)
    middle_index = length // 2
    return numbers[middle_index]

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    result = get_middle_element(sample_numbers)
    print(result)