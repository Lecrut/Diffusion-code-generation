def split_words(text: str) -> list[str]:
    return text.split()
if __name__ == '__main__':
    sample_text = "Hello world Python programming"
    result = split_words(sample_text)
    print(result)