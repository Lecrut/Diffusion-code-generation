def replace_whitespace_with_underscore(text: str) -> str:
    return text.replace(" ", "_")

if __name__ == '__main__':
    sample_string = "Hello World  Example"
    result = replace_whitespace_with_underscore(sample_string)
    print(result)