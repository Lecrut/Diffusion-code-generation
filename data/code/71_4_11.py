def get_middle_element(numbers):
    if not numbers:
        return None
    n = len(numbers)
    middle_index = n // 2
    return numbers[middle_index]

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    result = get_middle_element(sample_numbers)
    if result is not None:
        print(result)
    else:
        print("The list is empty.")