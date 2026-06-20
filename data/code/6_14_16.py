def replace_spaces_with_underscores(input_string):
    return input_string.replace(' ', '_')

if __name__ == '__main__':
    sample_strings = [
        "hello world",
        "python is great",
        "no spaces here",
        "multiple   spaces   between",
        " leading and trailing ",
        ""
    ]
    for sample in sample_strings:
        result = replace_spaces_with_underscores(sample)
        print(f"Input: '{sample}' -> Output: '{result}'")