def capitalize_words(text: str) -> str:
    return text.title()

if __name__ == '__main__':
    sample_input = "hello world python programming"
    result = capitalize_words(sample_input)
    print(result)