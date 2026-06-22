def has_unique_chars(s):
    return len(s) == len(set(s))

if __name__ == '__main__':
    print(has_unique_chars("abcdef"))
    print(has_unique_chars("hello"))
    print(has_unique_chars(""))
    print(has_unique_chars("a"))
    print(has_unique_chars("aa"))