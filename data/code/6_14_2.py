def replace_spaces_with_underscores(text: str) -> str:
    return text.replace(' ', '_')

if __name__ == '__main__':
    sample1 = "hello world"
    sample2 = "  multiple   spaces  "
    sample3 = "no_spaces"
    sample4 = ""

    print(replace_spaces_with_underscores(sample1))
    print(replace_spaces_with_underscores(sample2))
    print(replace_spaces_with_underscores(sample3))
    print(replace_spaces_with_underscores(sample4))