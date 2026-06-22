def print_list_with_indices(data):
    for index, value in enumerate(data):
        print(f"Index {index}: {value}")

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date", "elderberry"]
    print_list_with_indices(sample_strings)