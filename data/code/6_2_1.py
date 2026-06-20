def replace_whitespace_with_underscores(text: str) -> str:
    return text.replace(" ", "_").replace("\t", "_").replace("\n", "_").replace("\r", "_").replace("\v", "_").replace("\f", "_")

if __name__ == '__main__':
    sample_input = "Hello World\tNew\nLine"
    result = replace_whitespace_with_underscores(sample_input)
    print(result)