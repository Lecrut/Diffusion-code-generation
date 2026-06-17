def extract_first_letters(text):
    words = text.split()
    return ''.join(word[0].lower() for word in words if len(word) > 0)
if __name__ == '__main__':
    sample_text = "Hello World, Python Programming is Fun!"
    result = extract_first_letters(sample_text)
    print(result)