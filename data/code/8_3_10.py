def split_and_filter(s):
    return list(filter(lambda x: x.strip(), s.split(',')))

if __name__ == '__main__':
    sample = "apple, , banana,  , cherry"
    print(split_and_filter(sample))