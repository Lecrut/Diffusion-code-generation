LONG_WORD_THRESHOLD = 15

def is_word_long(word):
    return len(word) > LONG_WORD_THRESHOLD

if __name__ == '__main__':
    print(is_word_long("short"))
    print(is_word_long("thisisalongword"))
    print(is_word_long("a_very_long_string_example"))
    print(is_word_long("exactlyfifteen"))
    print(is_word_long(""))