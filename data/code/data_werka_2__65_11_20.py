def print_strings_with_index(strings):
    for index, string in enumerate(strings):
        print(f"Position {index}: {string}")

if __name__ == '__main__':
    SAMPLE_STRINGS = ["apple", "banana", "cherry", "date", "elderberry"]
    print_strings_with_index(SAMPLE_STRINGS)