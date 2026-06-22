def build_string(parts, separator=""):
    if not parts:
        return ""
    return separator.join(parts)

if __name__ == '__main__':
    sample_parts = ["Hello", "world", "this", "is", "a", "test"]
    no_separator_result = build_string(sample_parts)
    space_separator_result = build_string(sample_parts, " ")
    comma_separator_result = build_string(sample_parts, ",")
    
    print("No separator:", no_separator_result)
    print("Space separator:", space_separator_result)
    print("Comma separator:", comma_separator_result)