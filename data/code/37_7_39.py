def validate_strings(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError("Both inputs must be strings.")

def combine_strings(str1, str2):
    validate_strings(str1, str2)
    return f"{str1} {str2}"

if __name__ == '__main__':
    sample_str1 = "Good morning"
    sample_str2 = "Everyone"
    result = combine_strings(sample_str1, sample_str2)
    print(result)