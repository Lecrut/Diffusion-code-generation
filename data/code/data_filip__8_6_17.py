def split_and_strip(s):
    return [part.strip() for part in s.split(',') if part.strip()]

if __name__ == '__main__':
    sample = " apple , banana ,, cherry , orange "
    result = split_and_strip(sample)
    print(result)