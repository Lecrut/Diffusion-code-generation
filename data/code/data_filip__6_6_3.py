def replace_spaces_with_underscores(text):
    return text.replace(' ', '_')

if __name__ == '__main__':
    sample_strings = [
        "hello world",
        "this is a test",
        "no_spaces_here",
        "multiple   spaces   between",
        " leading and trailing ",
        ""
    ]
    for s in sample_strings:
        print(replace_spaces_with_underscores(s))