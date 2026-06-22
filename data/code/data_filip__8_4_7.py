def split_and_strip(s):
    return [token.strip() for token in s.split(',')]

if __name__ == '__main__':
    print(split_and_strip("hello, world, python"))