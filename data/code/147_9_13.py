def is_valid_list(input_list):
    return isinstance(input_list, list)

def sort_list(input_list):
    if not is_valid_list(input_list):
        raise ValueError("Input must be a list")
    return sorted(input_list)

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_list = sort_list(sample_list)
    print(sorted_list)