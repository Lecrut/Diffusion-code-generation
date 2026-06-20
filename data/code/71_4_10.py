def find_middle_element(numbers):
    if not numbers:
        raise ValueError("List is empty")
    length = len(numbers)
    mid_index = length // 2
    return numbers[mid_index]

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    try:
        print(find_middle_element(sample_numbers))
    except ValueError as e:
        print(e)