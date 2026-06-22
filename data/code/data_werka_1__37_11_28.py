def validate_strings(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError("Both inputs must be strings")

def combine_strings(str1, str2):
    validate_strings(str1, str2)
    return str1 + str2

if __name__ == '__main__':
    string_a = "Hello"
    string_b = "World"
    result = combine_strings(string_a, string_b)
    print(result)