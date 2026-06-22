def is_word_long(word):
    length_threshold = 6
    return len(word) > length_threshold

if __name__ == '__main__':
    sample_words = ['apple', 'banana', 'kiwi', 'strawberry']
    for word in sample_words:
        print(f"{word}: {is_word_long(word)}")