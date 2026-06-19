def validate_string(input_str):
    if not isinstance(input_str, str):
        raise ValueError("Input must be a string")

def combine_strings(str1, str2):
    validate_string(str1)
    validate_string(str2)
    return str1 + str2

if __name__ == '__main__':
    sample_str1 = "Good morning"
    sample_str2 = ", everyone!"
    combined_result = combine_strings(sample_str1, sample_str2)
    print(combined_result)