def build_string(parts, separator=""):
    return separator.join(parts)

if __name__ == '__main__':
    string_parts = ["Hello", "world", "this", "is", "a", "test"]
    separator_choice = ", "
    constructed_string = build_string(string_parts, separator_choice)
    print(constructed_string)