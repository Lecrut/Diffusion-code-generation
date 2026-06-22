def replace_spaces_with_underscores(s):
    return s.replace(' ', '_')

if __name__ == '__main__':
    sample_strings = [
        "hello world",
        "python is great",
        "no spaces here",
        "multiple   spaces   exist",
        " leading and trailing "
    ]
    for s in sample_strings:
        print(replace_spaces_with_underscores(s))