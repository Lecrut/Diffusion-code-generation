def is_long_word(word):
    return len(word) > 10

if __name__ == '__main__':
    test_words = ["short", "thisisalongword", "anotherword", "verylongwordexample"]
    for word in test_words:
        print(f"Is '{word}' long? {is_long_word(word)}")