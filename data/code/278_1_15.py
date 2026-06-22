def print_separately_with_index(strings):
    for index, string in enumerate(strings, start=1):
        print(f"{index}. {string}")

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry"]
    print_separately_with_index(sample_strings)