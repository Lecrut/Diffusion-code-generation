def extract_first_letters(text: str) -> str:
    words = text.split()
    if not words:
        return ""
    result_chars = [word[0] for word in words if word]
    return "".join(result_chars)
if __name__ == '__main__':
    sample_input = "Hello World Python Programming"
    result = extract_first_letters(sample_input)
    print(result)