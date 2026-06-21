def validate_input(data):
    if not isinstance(data, list) or not all(isinstance(item, str) for item in data):
        raise ValueError("Input must be a list of strings")

def sort_strings_case_insensitive(strings):
    validate_input(strings)
    return sorted(strings, key=lambda s: s.lower())

if __name__ == '__main__':
    sample_values = ["banana", "Apple", "cherry", "date"]
    print(sort_strings_case_insensitive(sample_values))