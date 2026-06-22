def is_word_long(word):
    return len(word) > 10

if __name__ == '__main__':
    sample_words = ["short", "thisisalongword", "anotherlongone", "medium", "verylongwordexample"]
    long_words = [w for w in sample_words if is_word_long(w)]
    print(long_words)