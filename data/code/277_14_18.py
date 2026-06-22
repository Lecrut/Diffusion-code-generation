def count_words(text):
    word_count = 0
    for char in text:
        if char == ' ':
            word_count += 1
    return word_count + 1

if __name__ == '__main__':
    sample_text = "Hello, World! This is a test string."
    print(count_words(sample_text))