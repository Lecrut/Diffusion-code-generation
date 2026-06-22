def validate_string(input_str):
    if not isinstance(input_str, str):
        raise ValueError("Input must be a string")

def combine_strings(str1, str2):
    validate_string(str1)
    validate_string(str2)
    return f"{str1} {str2}"

if __name__ == '__main__':
    sample_str_a = "Hello"
    sample_str_b = "World"
    combined_result = combine_strings(sample_str_a, sample_str_b)
    print(combined_result)