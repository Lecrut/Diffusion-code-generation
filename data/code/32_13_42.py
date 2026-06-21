def get_phrase_length(input_string):
    return len(input_string.strip())

if __name__ == '__main__':
    SAMPLE_VALUES = [
        "",
        "   ",
        "Hello, World!",
        "  Leading and trailing spaces  ",
        "NoSpacesHere",
        "1234567890",
        "\tTabs\tand\nnewlines\n",
        "Multiple     spaces"
    ]
    for value in SAMPLE_VALUES:
        print(get_phrase_length(value))