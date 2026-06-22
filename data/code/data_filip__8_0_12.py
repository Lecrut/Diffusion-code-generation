def split_commas(s):
    return [part for part in s.split(',') if part]

if __name__ == '__main__':
    print(split_commas("a,b,c"))
    print(split_commas(",a,,b,c,"))
    print(split_commas(""))
    print(split_commas("hello"))