def validate_input(iterable):
    if not all(isinstance(item, str) for item in iterable):
        raise ValueError("All elements in the list must be strings")

def print_separately_with_index(strings):
    validate_input(strings)
    for index, string in enumerate(strings, start=1):
        print(f"{index}. {string}")

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry"]
    print_separately_with_index(sample_strings)