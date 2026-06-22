def split_and_filter(s):
    return list(filter(lambda x: x.strip() != '', s.split(',')))

if __name__ == '__main__':
    sample_string = "apple, ,banana, ,cherry, , ,date"
    result = split_and_filter(sample_string)
    print(result)