def find_max_index(numbers):
    if not numbers:
        return None
    max_value = numbers[0]
    max_index = 0
    for index, value in enumerate(numbers[1:], start=1):
        if value > max_value:
            max_value = value
            max_index = index
    return max_index
if __name__ == '__main__':
    sample_numbers = [3, 5, 2, 8, 6]
    print(find_max_index(sample_numbers))