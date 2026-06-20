def replace_spaces_with_underscore(text: str) -> str:
    return text.replace(' ', '_')

if __name__ == '__main__':
    sample_text = "Hello World Python Code"
    result = replace_spaces_with_underscore(sample_text)
    print(result)