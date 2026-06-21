def validate_input(strings):
    if not isinstance(strings, list):
        raise ValueError("Input must be a list.")
    for item in strings:
        if not isinstance(item, str):
            raise ValueError("All items in the list must be strings.")

def sort_strings_by_length(strings):
    validate_input(strings)
    return sorted(strings, key=len)

if __name__ == '__main__':
    sample_values = ["strawberry", "blueberry", "raspberry", "blackberry", "a"]
    sorted_values = sort_strings_by_length(sample_values)
    print(sorted_values)