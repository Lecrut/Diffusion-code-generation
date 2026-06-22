def get_middle_element(numbers):
    if not numbers:
        raise ValueError("List is empty")
    length = len(numbers)
    mid_index = length // 2
    if length % 2 == 0:
        return numbers[mid_index - 1]
    return numbers[mid_index]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = get_middle_element(sample_data)
    print(result)