def find_all_words(text):
    words = set()
    current_word = []
    for char in text:
        if char.isalpha():
            current_word.append(char.lower())
        elif current_word:
            words.add(''.join(current_word))
            current_word = []
    if current_word:
        words.add(''.join(current_word))
    return words

if __name__ == '__main__':
    sample_string = "Hello world! This is a test, with Python programming."
    result = find_all_words(sample_string)
    print(result)