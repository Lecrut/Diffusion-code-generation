def merge_strings(a, b):
    if not isinstance(a, str) or not isinstance(b, str):
        raise ValueError("Both inputs must be strings")
    return a + b

if __name__ == '__main__':
    string_a = "Hello, "
    string_b = "World!"
    combined_string = merge_strings(string_a, string_b)
    print(combined_string)