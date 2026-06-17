def extract_first_letters(text: str) -> str:
    words = text.split()
    return ''.join(word[0].upper() for word in words if word)
if __name__ == '__main__':
    sample_input = "hello world python script"
    result = extract_first_letters(sample_input)
    print(result)