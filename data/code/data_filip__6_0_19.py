def replace_spaces(text: str) -> str:
    return text.replace(" ", "_")

if __name__ == '__main__':
    sample_text = "Hello World Python"
    result = replace_spaces(sample_text)
    print(result)