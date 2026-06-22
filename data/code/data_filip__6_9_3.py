def replace_spaces_with_underscores(s: str) -> str:
    return s.replace(' ', '_')

if __name__ == '__main__':
    sample_text = "Hello World from Python"
    result = replace_spaces_with_underscores(sample_text)
    print(result)