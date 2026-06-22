def is_valid_string_list(input_list):
    return all(isinstance(item, str) for item in input_list)

def reverse_strings(string_list):
    if not is_valid_string_list(string_list):
        raise ValueError("Input must be a list of strings")
    return [s[::-1] for s in string_list]

if __name__ == '__main__':
    sample_values = ["hello", "world", "!"]
    try:
        reversed_list = reverse_strings(sample_values)
        print(reversed_list)
    except ValueError as e:
        print(e)