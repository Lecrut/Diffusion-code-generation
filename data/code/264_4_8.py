def find_distinct_words(text):
    words = set()
    current_word = ""
    for char in text:
        if char.isalpha():
            current_word += char
        elif current_word:
            words.add(current_word.lower())
            current_word = ""
    if current_word:
        words.add(current_word.lower())
    return words

if __name__ == '__main__':
    sample_string = "Hello, World! This is a test string with repeated words and some punctuation."
    result = find_distinct_words(sample_string)
    print(result)