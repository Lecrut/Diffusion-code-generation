def is_unique(s):
    return len(set(s)) == len(s)

if __name__ == '__main__':
    print(is_unique("hello"))
    print(is_unique("world"))
    print(is_unique(""))
    print(is_unique("a"))
    print(is_unique("abcdefg"))
    print(is_unique("aabbcc"))