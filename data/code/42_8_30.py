def build_string(parts, separator=""):
    return separator.join(parts)

if __name__ == '__main__':
    string_parts = ["Hello", "world", "this", "is", "a", "test"]
    separator_choice = ", "
    result = build_string(string_parts, separator_choice)
    print(result)