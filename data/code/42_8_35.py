def build_string(parts, separator=""):
    if not parts:
        return ""
    return separator.join(parts)

if __name__ == '__main__':
    sample_parts = ["Hello", "world", "this", "is", "a", "test"]
    result_with_space = build_string(sample_parts, " ")
    result_with_comma = build_string(sample_parts, ",")
    result_no_separator = build_string(sample_parts)
    
    print("With space separator:", result_with_space)
    print("With comma separator:", result_with_comma)
    print("No separator:", result_no_separator)