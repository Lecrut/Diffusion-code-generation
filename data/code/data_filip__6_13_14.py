def replace_spaces_with_underscore(text: str) -> str:
    return text.replace(' ', '_')

if __name__ == '__main__':
    sample_text = "This is a constant string with spaces."
    result = replace_spaces_with_underscore(sample_text)
    print(result)