def is_word_long(word, threshold=10):
    if not isinstance(word, str) or not isinstance(threshold, int):
        raise ValueError('Invalid input type')
    return len(word) > threshold
if __name__ == '__main__':
    print(is_word_long('short'))
    print(is_word_long('thisisalongword'))