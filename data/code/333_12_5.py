def extract_first_letters(text):
    words = text.split()
    return [word[0].upper() for word in words if len(word) > 0]
if __name__ == '__main__':
    sample_input = "hello world this is a test string"
    result = extract_first_letters(sample_input)
    print("".join(result))