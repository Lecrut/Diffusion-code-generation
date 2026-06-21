def flatten_and_check(data, value):
    flattened = [item for sublist in data for item in sublist if isinstance(item, list)]
    return value in flattened

if __name__ == '__main__':
    sample_list = [
        [1, 2, 3],
        [4, 5],
        [6, 7, 8, 9]
    ]
    value_to_find = 5
    result = flatten_and_check(sample_list, value_to_find)
    print(f"Checking for '{value_to_find}' in nested list: {result}")