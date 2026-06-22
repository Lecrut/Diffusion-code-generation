def validate_list(input_list):
    if not isinstance(input_list, list):
        raise ValueError("Input must be a list")

def print_items_with_index(input_list):
    validate_list(input_list)
    for index, item in enumerate(input_list):
        print(f"{index}: {item}")

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print_items_with_index(sample_list)