def extract_first_letters(text):
    words = text.split()
    return ''.join(word[0].lower() for word in words if len(word) > 0)
if __name__ == '__main__':
    sample_input = "Hello World Python Programming"
    result = extract_first_letters(sample_input)
    print(result)