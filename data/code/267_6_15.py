def is_word_long(word, threshold=10):
    return len(word) > threshold

if __name__ == '__main__':
    words = ["short", "thisisalongword", "anotherword", "verylongwordexample"]
    for word in words:
        print(is_word_long(word))