def get_phrase_length(input_string):
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
        "\tTabs\tand\nnewlines\n"
    ]
    for value in sample_values:
        length = get_phrase_length(value)
        print(f"Input: '{value}' -> Length: {length}")