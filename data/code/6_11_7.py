def replace_spaces_with_underscores(text: str) -> str:
    return text.replace(' ', '_')

if __name__ == '__main__':
    sample_text = "Hello World This Is A Test"
    result = replace_spaces_with_underscores(sample_text)
    print(result)