def validate_input(iterable):
    if not all(isinstance(item, str) for item in iterable):
        raise ValueError("All elements in the list must be strings")

def print_separately_with_index(iterable):
    validate_input(iterable)
    for index, item in enumerate(iterable, start=1):
        print(f"{index}. {item}")

if __name__ == '__main__':
    sample_data = ["apple", "banana", "cherry"]
    print_separately_with_index(sample_data)