def has_unique_chars(s):
    return len(set(s)) == len(s)

if __name__ == '__main__':
    print(has_unique_chars("abcde"))
    print(has_unique_chars("hello"))