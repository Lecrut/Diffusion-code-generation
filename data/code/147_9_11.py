def is_valid_list(input_list):
    if not isinstance(input_list, list):
        raise ValueError("Input must be a list")
    for item in input_list:
        if not isinstance(item, (int, float)):
            raise ValueError("List items must be integers or floats")

def sort_numbers(numbers_list):
    is_valid_list(numbers_list)
    return sorted(numbers_list)

if __name__ == '__main__':
    sample_list = [3.5, 1, 4.2, 0, -2]
    sorted_list = sort_numbers(sample_list)
    print(sorted_list)