def extract_first_letters(text):
    words = text.split()
    result_chars = []
    for word in words:
        if not word:                                                          
            continue
        first_char = word[0]
        if first_char.isalpha():
            result_chars.append(first_char)
    return ''.join(result_chars)
if __name__ == '__main__':
    samples = [
        "Hello World",
        "Python Programming is Fun!",
        "   Multiple spaces between words"
    ]
    for sample in samples:
        processed_output = extract_first_letters(sample)
        print(processed_output)