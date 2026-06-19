def print_strings_with_indices(strings):
    for index, string in enumerate(strings):
        print(f"{index}: {string}")

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    print_strings_with_indices(sample_strings)