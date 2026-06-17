def split_words(text: str) -> list[str]:
    return text.split()
if __name__ == '__main__':
    sample_text = "Hello World Python Programming"
    words = split_words(sample_text)
    print(words)
    if len(words) != 4 or not isinstance(words, list):
        exit(1)