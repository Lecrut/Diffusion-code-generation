def split_words(text: str) -> list[str]:
    return text.split()
if __name__ == '__main__':
    sample_text = "Hello World This is a Python script"
    words = split_words(sample_text)
    print(words)