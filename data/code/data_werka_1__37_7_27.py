def combine_strings(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError("Both inputs must be strings")
    return f"{str1} {str2}"

if __name__ == '__main__':
    string_a = "Good"
    string_b = "Morning"
    result = combine_strings(string_a, string_b)
    print(result)