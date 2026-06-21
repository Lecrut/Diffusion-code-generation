def find_max_index(numbers):
    max_value = numbers[0]
    max_index = 0
    for index, value in enumerate(numbers):
        if value > max_value:
            max_value = value
            max_index = index
    return max_index

if __name__ == '__main__':
    sample_list = [3, 5, 1, 2, 4]
    print(find_max_index(sample_list))