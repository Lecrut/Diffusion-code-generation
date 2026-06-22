def is_unique(s):
    return len(set(s)) == len(s)

if __name__ == '__main__':
    print(is_unique("abcdef"))
    print(is_unique("hello"))