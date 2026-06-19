def print_list_with_indices(mixed_list):
    for index, element in enumerate(mixed_list):
        print(f"Index {index}: {element}")

if __name__ == '__main__':
    sample_list = [42, "hello", 3.14, True, None]
    print_list_with_indices(sample_list)