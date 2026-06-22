def has_duplicates(s):
    return len(s) != len(set(s))

if __name__ == '__main__':
    print(has_duplicates("hello"))
    print(has_duplicates("world"))
    print(has_duplicates("abcdefg"))
    print(has_duplicates("aabbcc"))