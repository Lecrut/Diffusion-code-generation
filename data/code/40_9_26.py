def extract_first_letters(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    words = text.split()
    first_letters = []
    for word in words:
        if word:
            first_letters.append(word[0])
    return first_letters

if __name__ == '__main__':
    sample_texts = [
        "Hello world",
        "",
        "   \t ",
        "Single",
        "  Test case ",
        "One   two   three",
        "Hello, world!"
    ]
    
    for text in sample_texts:
        print(extract_first_letters(text))