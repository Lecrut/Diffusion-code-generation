def is_word_long(s):
    return len(s) > 15

if __name__ == '__main__':
    words = ["short", "thisisalongword", "a_very_long_string_example", "exactlyfifteen", ""]
    for word in words:
        print(is_word_long(word))