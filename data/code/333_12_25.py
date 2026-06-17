def extract_first_letters(text):
    words = text.split()
    return ''.join(word[0].upper() for word in words if word)
if __name__ == '__main__':
    sample_input = "hello world this is a test"
    result = extract_first_letters(sample_input)
    print(result)