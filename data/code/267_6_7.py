THRESHOLD = 10

def is_long_word(word):
    return len(word) > THRESHOLD

if __name__ == '__main__':
    sample_words = ["short", "thisisalongword", "anotherword", "verylongwordexample"]
    for word in sample_words:
        print(is_long_word(word))