def extract_words(text):
    words = []
    current_word = ""
    for char in text:
        if char.isalpha():
            current_word += char.lower()
        else:
            if current_word:
                words.append(current_word)
                current_word = ""
    if current_word:
        words.append(current_word)
    return set(words)

if __name__ == '__main__':
    sample_string = "Hello, world! This is a test string with some punctuation."
    distinct_words = extract_words(sample_string)
    print(distinct_words)