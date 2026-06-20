def split_and_strip(s):
    return [token.strip() for token in s.split(',')]
if __name__ == '__main__':
    sample = ' hello , world , python '
    result = split_and_strip(sample)
    print(result)