def is_word_long(word):
    word_length = len(word)
    return word_length > 10

if __name__ == '__main__':
    sample_words = {
        "short": False,
        "thisisalongstring": True,
        "onlyletters": False,
        "this has a space": True,
        "abcdefghij": False,
        "a" * 11: True,
        "1234567890": False
    }
    
    for word, expected in sample_words.items():
        result = is_word_long(word)
        print(f"Input: '{word}', Expected: {expected}, Result: {result}")