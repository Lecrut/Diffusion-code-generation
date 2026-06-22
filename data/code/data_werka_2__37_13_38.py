def merge_strings(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError("Both inputs must be strings")
    return str1 + str2

if __name__ == '__main__':
    string_a = "Hello"
    string_b = "World"
    merged_string = merge_strings(string_a, string_b)
    print(merged_string)