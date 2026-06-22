def replace_spaces_with_underscores(s: str) -> str:
    return s.replace(' ', '_')

if __name__ == '__main__':
    sample = "hello world this is a test"
    result = replace_spaces_with_underscores(sample)
    print(result)