def replace_spaces_with_underscores(text):
    return text.replace(' ', '_')

if __name__ == '__main__':
    sample_strings = [
        "hello world",
        "python programming language",
        "no spaces here",
        "multiple   spaces   between words",
        ""
    ]
    for sample in sample_strings:
        print(replace_spaces_with_underscores(sample))