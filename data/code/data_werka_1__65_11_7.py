def print_strings_with_indices(strings):
    for index, string in enumerate(strings):
        print(f"Index {index}: {string}")

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date", "elderberry"]
    print_strings_with_indices(sample_list)