def validate_string_list(input_list):
    if not all(isinstance(item, str) for item in input_list):
        raise ValueError("All elements in the list must be strings")

def reverse_strings(string_list):
    validate_string_list(string_list)
    for s in string_list:
        print(s[::-1])

if __name__ == '__main__':
    sample_values = ["hello", "world", "!"]
    reverse_strings(sample_values)