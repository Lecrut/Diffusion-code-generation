def extract_words(text: str) -> list[str]:
    words = text.split()
    return words
if __name__ == '__main__':
    sample_string = "This is a sample sentence for word extraction"
    result = extract_words(sample_string)
    print(result)