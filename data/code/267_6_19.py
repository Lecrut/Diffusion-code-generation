def is_word_long(word):
    word_length_threshold = 10
    return len(word) > word_length_threshold

if __name__ == '__main__':
    sample_words = ["short", "thisisalongword", "anotherword", "verylongwordexample"]
    for word in sample_words:
        print(f"Is '{word}' long? {is_word_long(word)}")