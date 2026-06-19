def build_string(parts, separator=""):
    return separator.join(parts)

if __name__ == '__main__':
    string_parts = ["Hello", "world", "from", "Alibaba"]
    separator = ", "
    result = build_string(string_parts, separator)
    print(result)