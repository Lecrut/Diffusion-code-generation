def print_separated_with_index(strings):
    for index, string in enumerate(strings, start=1):
        print(f"{index}. {string}")

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry"]
    print_separated_with_index(sample_strings)