def get_phrase_length(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
    def is_empty_or_whitespace(s):
        return s.strip() == ""
    
    if is_empty_or_whitespace(input_string):
        return 0
    
    stripped_string = input_string.strip()
    return len(stripped_string)

if __name__ == '__main__':
    sample_values = [
        "",
        "   ",
        "Hello, World!",
        "  Leading and trailing spaces  ",
        "\tTabs\tand\nnewlines\n",
        "Multiple     spaces",
        "NoSpacesHere",
        "1234567890"
    ]
    for value in sample_values:
        print(get_phrase_length(value))