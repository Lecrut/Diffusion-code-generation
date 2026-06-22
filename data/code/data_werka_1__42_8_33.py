def build_string(parts, separator=""):
    return separator.join(parts)

if __name__ == '__main__':
    SAMPLE_PARTS = ["Hello", "world", "this", "is", "a", "test"]
    SEPARATOR_NO_SPACE = ""
    SEPARATOR_SPACE = " "
    SEPARATOR_COMMA = ","
    
    result_no_space = build_string(SAMPLE_PARTS, SEPARATOR_NO_SPACE)
    result_with_space = build_string(SAMPLE_PARTS, SEPARATOR_SPACE)
    result_with_comma = build_string(SAMPLE_PARTS, SEPARATOR_COMMA)
    
    print(result_no_space)
    print(result_with_space)
    print(result_with_comma)