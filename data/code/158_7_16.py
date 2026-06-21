def is_valid_input(item):
    return isinstance(item, int)

def filter_even_numbers(mixed_list):
    if not all(is_valid_input(item) for item in mixed_list):
        raise ValueError("All items in the list must be integers.")
    return [item for item in mixed_list if item % 2 == 0]

if __name__ == '__main__':
    sample_values = [1, 2, 'a', 3, 4.5, 6]
    try:
        print(filter_even_numbers(sample_values))
    except ValueError as e:
        print(e)