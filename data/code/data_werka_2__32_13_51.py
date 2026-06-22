def get_phrase_length(input_string):
    def is_valid_input(s):
        return isinstance(s, str)
    
    if not is_valid_input(input_string):
        raise ValueError("Input must be a string")
    
    stripped_string = input_string.strip()
    return len(stripped_string)

if __name__ == '__main__':
    sample_values = [
        "",
        "   ",
        "Hello, World!",
        "  Leading and trailing spaces  ",
        "NoSpacesHere",
        "1234567890",
        "\tTabs\tand\nnewlines\n",
        "Multiple     spaces"
    ]
    for value in sample_values:
        print(get_phrase_length(value))