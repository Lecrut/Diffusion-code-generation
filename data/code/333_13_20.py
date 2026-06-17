def extract_first_letters(text: str) -> list[str]:
    return [word[0] for word in text.split() if len(word) > 1]
if __name__ == '__main__':
    print(extract_first_letters("Hello World Python Programming"))