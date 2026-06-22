def is_word_long(word):
    word_length_threshold = 10
    return len(word) > word_length_threshold

if __name__ == '__main__':
    sample_words = ["short", "longerword", "thisisalongword", "medium", "verylongwordexample"]
    long_words = [word for word in sample_words if is_word_long(word)]
    print(long_words)