def get_middle_element(numbers):
    if not numbers:
        raise ValueError("List is empty")
    mid_index = len(numbers) // 2
    return numbers[mid_index]

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    result = get_middle_element(sample_numbers)
    print(result)