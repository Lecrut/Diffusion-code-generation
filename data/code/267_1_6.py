def is_word_long(word):
    min_length = 15
    return len(word) > min_length

if __name__ == '__main__':
    sample_words = ["short", "thisisalongword", "a_very_long_string_example", "exactlyfifteen", ""]
    for word in sample_words:
        print(f"Is '{word}' long? {is_word_long(word)}")