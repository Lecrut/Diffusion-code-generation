def replace_spaces_with_underscores(text):
    return text.replace(' ', '_')

if __name__ == '__main__':
    sample_strings = [
        "hello world",
        "no spaces here",
        "multiple   spaces   between words",
        "",
        "leading space",
        "trailing space ",
        "  both ends  "
    ]
    for sample in sample_strings:
        result = replace_spaces_with_underscores(sample)
        print(result)