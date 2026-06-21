def find_max_index(numbers):
    max_value = float('-inf')
    max_index = -1
    for index, number in enumerate(numbers):
        if number > max_value:
            max_value = number
            max_index = index
    return max_index

if __name__ == '__main__':
    sample_numbers = [3, 5, 2, 8, 1]
    max_idx = find_max_index(sample_numbers)
    print(max_idx)