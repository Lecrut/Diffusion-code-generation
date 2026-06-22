def validate_input(input_list):
    if not isinstance(input_list, list) or not all(isinstance(item, str) for item in input_list):
        raise ValueError("Input must be a list of strings")

def reverse_strings(string_list):
    validate_input(string_list)
    return string_list[::-1]

if __name__ == '__main__':
    sample_values = ["python", "programming", "is", "fun"]
    reversed_values = reverse_strings(sample_values)
    for value in reversed_values:
        print(value)