def is_long_word(word, min_length=10):
    return len(word) > min_length

if __name__ == '__main__':
    word_short = "example"
    word_long = "thisisaverylongwordthatexceedsthenormallength"
    
    print(f"Is '{word_short}' a long word? {is_long_word(word_short)}")
    print(f"Is '{word_long}' a long word? {is_long_word(word_long, min_length=15)}")