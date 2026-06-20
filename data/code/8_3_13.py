def split_and_filter(s):
    return list(filter(lambda part: part.strip(), s.split(',')))

if __name__ == '__main__':
    sample = "apple, , banana,  , cherry"
    result = split_and_filter(sample)
    print(result)