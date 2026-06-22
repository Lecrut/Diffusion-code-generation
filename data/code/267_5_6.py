def is_long_word(word):
    return len(word) > 10

if __name__ == '__main__':
    sample_words = ["short", "thisisalongword", "anotherone", "verylongwordexample", "medium"]
    long_words = [word for word in sample_words if is_long_word(word)]
    print(long_words)