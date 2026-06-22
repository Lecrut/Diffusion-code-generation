def get_middle_element(numbers):
    if not numbers:
        raise ValueError("List is empty")
    length = len(numbers)
    middle_index = length // 2
    if length % 2 == 0:
        return (numbers[middle_index - 1] + numbers[middle_index]) / 2
    return numbers[middle_index]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_middle_element(sample_list)
    print(result)