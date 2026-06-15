def is_word_long(s):
    return len(s) > 15
if __name__ == '__main__':
    print(is_word_long("short"))
    print(is_word_long("thisisalongword"))
    print(is_word_long("a_very_long_string_example"))
    print(is_word_long("exactlyfifteen"))
    print(is_word_long(""))