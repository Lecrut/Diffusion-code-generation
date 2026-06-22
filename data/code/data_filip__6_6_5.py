def convert_spaces_to_underscores(text):
    return text.replace(' ', '_')

if __name__ == '__main__':
    sample_strings = [
        "hello world",
        "this is a test",
        "no internal spaces",
        "  leading and trailing  ",
        "multiple   spaces   here"
    ]
    for s in sample_strings:
        result = convert_spaces_to_underscores(s)
        print(result)