def split_and_filter(s):
    parts = s.split(',')
    result = list(filter(lambda x: x.strip() != '', parts))
    return result

if __name__ == '__main__':
    sample_string = 'a, , b, ,c, d '
    result = split_and_filter(sample_string)
    print(result)