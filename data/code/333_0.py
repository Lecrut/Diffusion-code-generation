def extract_first_letters(text: str) -> str:
    return "".join(word[0] for word in text.split())
if __name__ == '__main__':
    sample_string = "This is a sample string for testing purposes"
    result = extract_first_letters(sample_string)
    print(result)