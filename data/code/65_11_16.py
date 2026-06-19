def iterate_and_print_with_index(data):
    for index, element in enumerate(data):
        print(f"Index {index}: {element}")

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry', 'date']
    iterate_and_print_with_index(sample_list)