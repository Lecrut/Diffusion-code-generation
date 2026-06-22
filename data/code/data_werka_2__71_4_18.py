def get_middle_element(numbers):
    if not numbers:
        raise ValueError("The list is empty.")
    length = len(numbers)
    mid_index = length // 2
    return numbers[mid_index]

if __name__ == '__main__':
    sample_values = [5, 15, 25, 35, 45, 55, 65]
    result = get_middle_element(sample_values)
    print(result)