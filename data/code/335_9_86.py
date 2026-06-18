def split_words(text: str) -> list[str]:
    return text.split()
if __name__ == '__main__':
    sample_text = "Hello world! This is a test string with multiple words."
    result = split_words(sample_text)
    print(result)
    assert len(result) > 0, "Split should not be empty"
    exit(0)