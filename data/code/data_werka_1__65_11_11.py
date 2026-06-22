def print_strings_with_indices(strings):
    for index, string in enumerate(strings):
        print(f"Index {index}: {string}")

if __name__ == '__main__':
    SAMPLE_STRINGS = ["apple", "banana", "cherry", "date", "elderberry"]
    print_strings_with_indices(SAMPLE_STRINGS)