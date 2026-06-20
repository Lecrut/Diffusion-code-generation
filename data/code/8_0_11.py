def split_commas(s):
    return [part for part in s.split(',') if part]

if __name__ == '__main__':
    result = split_commas("a,,b, c,")
    print(result)