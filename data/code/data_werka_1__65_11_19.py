def iterate_and_print_with_index(strings):
    for index, string in enumerate(strings):
        print(f"Index {index}: {string}")

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    iterate_and_print_with_index(sample_strings)