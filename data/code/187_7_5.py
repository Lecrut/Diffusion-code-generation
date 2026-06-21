def find_max_with_index(numbers):
    max_value = float('-inf')
    max_index = -1
    for index, value in enumerate(numbers):
        if value > max_value:
            max_value = value
            max_index = index
    return (max_value, max_index)
if __name__ == '__main__':
    sample_numbers = [3, 5, 2, 9, 8]
    result = find_max_with_index(sample_numbers)
    print(result)