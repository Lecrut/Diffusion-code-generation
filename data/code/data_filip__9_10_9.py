def strip_whitespace(text: str) -> str:
    return text.strip()
if __name__ == '__main__':
    sample1 = '  hello world  '
    sample2 = '\t\nfoo\n\t'
    sample3 = 'no_extra_space'
    sample4 = '   leading_only'
    sample5 = 'trailing_only   '
    print(strip_whitespace(sample1))
    print(strip_whitespace(sample2))
    print(strip_whitespace(sample3))
    print(strip_whitespace(sample4))
    print(strip_whitespace(sample5))