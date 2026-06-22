def swap_spaces_for_underscores(s):
    return s.replace(' ', '_')

if __name__ == '__main__':
    sample_strings = [
        "hello world",
        "python programming",
        "no_spaces_here",
        "multiple   spaces",
        " leading and trailing ",
        "",
        " "
    ]
    for sample in sample_strings:
        result = swap_spaces_for_underscores(sample)
        print(repr(result))