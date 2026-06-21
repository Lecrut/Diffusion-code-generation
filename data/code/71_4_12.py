def get_middle_element(numbers):
    if not numbers:
        raise ValueError("List must not be empty")
    length = len(numbers)
    middle_index = length // 2
    return numbers[middle_index]

if __name__ == '__main__':
    SAMPLE_LIST = [1, 2, 3, 4, 5]
    result = get_middle_element(SAMPLE_LIST)
    print(result)