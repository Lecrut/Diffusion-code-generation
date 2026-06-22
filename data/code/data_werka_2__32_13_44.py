def get_phrase_length(input_string):
    if not input_string.strip():
        return 0
    return len(input_string)

if __name__ == '__main__':
    sample_values = [
        "",
        "   ",
        "Hello, World!",
        "  Leading and trailing spaces  ",
        "NoSpacesHere",
        "1234567890"
    ]
    for value in sample_values:
        print(get_phrase_length(value))