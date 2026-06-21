def find_max_with_index(numbers):
    max_value = float('-inf')
    max_index = -1
    for index, number in enumerate(numbers):
        if number > max_value:
            max_value = number
            max_index = index
    return max_value, max_index

if __name__ == '__main__':
    sample_numbers = [3, 5, 2, 8, 6]
    result = find_max_with_index(sample_numbers)
    print(result)