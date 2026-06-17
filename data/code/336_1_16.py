def has_repeated_chars(s):
    return len(set(s)) != len(s)
if __name__ == '__main__':
    print(has_repeated_chars("hello"))
    print(has_repeated_chars("world"))
    exit(0)