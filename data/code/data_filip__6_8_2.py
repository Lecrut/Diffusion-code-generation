def swap_spaces_for_underscores(s):
    return s.replace(' ', '_')

if __name__ == '__main__':
    sample_strings = [
        "hello world",
        "no spaces here",
        "  multiple   spaces  ",
        "",
        "single",
        "trailing space ",
        " leading space"
    ]
    for sample in sample_strings:
        print(swap_spaces_for_underscores(sample))