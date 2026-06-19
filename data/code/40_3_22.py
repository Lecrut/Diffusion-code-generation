def extract_initials(text: str) -> str:
    try:
        return ' '.join(word[0] if word else '' for word in text.split())
    except AttributeError as e:
        raise ValueError("Input must be a string") from e

if __name__ == '__main__':
    sample = "Hello World! Python is great."
    result = extract_initials(sample)
    print(result)