def print_list_with_index(input_list):
    if not isinstance(input_list, list):
        raise ValueError("Input must be a list")
    
    for index, item in enumerate(input_list):
        print(f"{index}: {item}")

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print_list_with_index(sample_list)