def validate_strings(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError("Both inputs must be strings.")

def concatenate_strings(str1, str2):
    validate_strings(str1, str2)
    return f"{str1}{str2}"

if __name__ == '__main__':
    string_a = "Good evening, "
    string_b = "World"
    result = concatenate_strings(string_a, string_b)
    print(result)