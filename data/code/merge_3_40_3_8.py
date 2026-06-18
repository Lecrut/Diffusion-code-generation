def extract_first_letters(text: str) -> str:
    return ' '.join(word[0] if word else '' for word in text.split())

if __name__ == '__main__':
    sample = "hello world this is a test string"
    result = extract_first_letters(sample)
    print(result)