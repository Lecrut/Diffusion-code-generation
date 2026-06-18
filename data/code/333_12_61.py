def extract_first_letters(text: str) -> list[str]:
    words = text.split()
    return [word[0] for word in words if word]
if __name__ == '__main__':
    sample_input = "Hello World Python Programming"
    result = extract_first_letters(sample_input)
    print("".join(result))