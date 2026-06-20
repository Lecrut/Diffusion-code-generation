def replace_internal_spaces_with_underscores(text):
    return text.replace(' ', '_')

if __name__ == '__main__':
    sample_strings = [
        "hello world",
        "no spaces",
        "multiple   spaces   here",
        " leading and trailing ",
        ""
    ]
    for s in sample_strings:
        result = replace_internal_spaces_with_underscores(s)
        print(result)