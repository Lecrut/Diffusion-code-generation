def extract_first_letters(text):
    return ''.join(word[0] for word in text.split() if word)
if __name__ == '__main__':
    sample = "Hello World Python Programming"
    result = extract_first_letters(sample)
    print(result)