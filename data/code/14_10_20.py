def has_unique_characters(s):
    return len(s) == len(set(s))

if __name__ == '__main__':
    print(has_unique_characters('abcdef'))
    print(has_unique_characters('hello'))