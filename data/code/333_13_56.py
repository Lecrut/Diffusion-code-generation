def extract_first_letters(text: str) -> list[str]:
    return [word[0] for word in text.split() if word]
if __name__ == '__main__':
    sample_text = "Hello World Python Programming"
    result = extract_first_letters(sample_text)
    print("".join(result))