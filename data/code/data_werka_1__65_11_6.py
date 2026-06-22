def print_strings_with_index(strings):
    for index, string in enumerate(strings):
        print(f"{index}: {string}")

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    print_strings_with_index(sample_strings)