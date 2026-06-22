def replace_whitespace_with_underscores(text: str) -> str:
    return text.replace(" ", "_").replace("\t", "_").replace("\n", "_").replace("\r", "_").replace("\f", "_").replace("\v", "_")

if __name__ == '__main__':
    sample_string = "Hello World\nThis is a\ttest"
    result = replace_whitespace_with_underscores(sample_string)
    print(result)