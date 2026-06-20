def split_and_strip(s):
    for item in s.split(','):
        stripped = item.strip()
        if stripped:
            yield stripped

if __name__ == '__main__':
    sample = " apple , banana ,, cherry , "
    result = list(split_and_strip(sample))
    print(result)