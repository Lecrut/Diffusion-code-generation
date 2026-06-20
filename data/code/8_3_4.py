def split_and_filter(string):
    return list(filter(lambda s: s.strip(), string.split(',')))

if __name__ == '__main__':
    sample = "apple, , banana, , cherry"
    result = split_and_filter(sample)
    print(result)