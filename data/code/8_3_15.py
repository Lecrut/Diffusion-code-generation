def split_and_filter(s):
    parts = s.split(',')
    result = list(filter(lambda part: part.strip(), parts))
    return result

if __name__ == '__main__':
    sample_string = "apple, ,banana,,cherry, ,date"
    print(split_and_filter(sample_string))