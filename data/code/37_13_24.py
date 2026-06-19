def validate_strings(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError("Both inputs must be strings")

def join_strings_optimized(str1, str2):
    validate_strings(str1, str2)
    result = ''.join([str1, str2])
    return result

if __name__ == '__main__':
    string_a = "Hello"
    string_b = "World"
    joined_string = join_strings_optimized(string_a, string_b)
    print(joined_string)