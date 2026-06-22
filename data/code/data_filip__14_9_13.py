def has_unique_characters(s):
    return len(set(s)) == len(s)

if __name__ == '__main__':
    print(has_unique_characters('abcde'))
    print(has_unique_characters('hello'))
    print(has_unique_characters(''))
    print(has_unique_characters('a'))
    print(has_unique_characters('aabbcc'))