MAX_VALUE_INDEX = 'max_value_index'

def find_max_value_index(numbers):
    return MAX_VALUE_INDEX, numbers.index(max(numbers))

if __name__ == '__main__':
    sample_values = [34, 12, 89, 76, 15]
    result_key, max_index = find_max_value_index(sample_values)
    print(f"{result_key}: {max_index}")