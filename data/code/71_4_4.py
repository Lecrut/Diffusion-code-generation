def get_middle_element(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    length = len(numbers)
    middle_index = length // 2
    return numbers[middle_index]

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    try:
        print(get_middle_element(sample_numbers))
    except ValueError as e:
        print(e)