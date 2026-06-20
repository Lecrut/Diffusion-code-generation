def replace_spaces_with_underscores(text):
    return text.replace(' ', '_')

if __name__ == '__main__':
    sample_strings = [
        "hello world",
        "no_spaces_here",
        "multiple   spaces   between",
        " leading and trailing ",
        "",
        "Python is great"
    ]
    for sample in sample_strings:
        result = replace_spaces_with_underscores(sample)
        print(result)