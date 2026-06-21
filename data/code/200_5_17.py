MAX_VALUE_INDEX = 'max_value_index'

def find_max_value_index(numbers):
    max_index = 0
    max_value = numbers[0]
    for index, number in enumerate(numbers):
        if number > max_value:
            max_value = number
            max_index = index
    return {MAX_VALUE_INDEX: max_index}

if __name__ == '__main__':
    sample_numbers = [3, 5, 1, 2, 4]
    result = find_max_value_index(sample_numbers)
    print(result[MAX_VALUE_INDEX])