def convert_spaces_to_underscores(text: str) -> str:
    return text.replace(' ', '_')

if __name__ == '__main__':
    sample_text = "hello world python"
    result = convert_spaces_to_underscores(sample_text)
    print(result)