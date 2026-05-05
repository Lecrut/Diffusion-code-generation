def print_indexed_strings(string_list):
    for index, item in enumerate(string_list):
        print(f"Index {index}: {item}")
if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date", "elderberry"]
    print_indexed_strings(sample_strings)