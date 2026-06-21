def get_phrase_length(input_string):
    stripped_input = input_string.strip()
    length_of_stripped_input = len(stripped_input)
    return length_of_stripped_input

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