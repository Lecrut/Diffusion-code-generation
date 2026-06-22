def print_items_with_index(input_list):
    for index, item in enumerate(input_list):
        print(f"{index}: {item}")

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    print_items_with_index(sample_list)