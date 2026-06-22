def capitalize_words(text: str) -> str:
    return text.title()

if __name__ == '__main__':
    sample_text = "hello world from python"
    result = capitalize_words(sample_text)
    print(result)