LONG_WORD_THRESHOLD = 10

def is_long_word(word):
    return len(word) > LONG_WORD_THRESHOLD

if __name__ == '__main__':
    sample_words = ["short", "longerword", "thisisalongword", "medium", "verylongwordexample"]
    long_words = [word for word in sample_words if is_long_word(word)]
    print(long_words)