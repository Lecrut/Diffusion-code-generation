def validate_strings(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError("Both arguments must be strings")

def combine_strings_optimized(str1, str2):
    validate_strings(str1, str2)
    return ''.join([str1, str2])

if __name__ == '__main__':
    string_a = "Hello, "
    string_b = "World!"
    result = combine_strings_optimized(string_a, string_b)
    print(result)