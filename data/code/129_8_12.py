def validate_data(data):
    if not all(isinstance(item, (str, int)) for item in data):
        raise ValueError("All elements must be either strings or integers")

def convert_to_strings(data):
    return [str(item) for item in data]

def sort_mixed_data(data):
    validate_data(data)
    string_data = convert_to_strings(data)
    return sorted(string_data)

if __name__ == '__main__':
    mixed_data = ['apple', 3, 'banana', 1, 'cherry', 2]
    sorted_data = sort_mixed_data(mixed_data)
    print(sorted_data)