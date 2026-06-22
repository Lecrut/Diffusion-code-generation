import re

def split_and_filter_string(s):
    return list(filter(lambda x: x.strip(), s.split(',')))

if __name__ == '__main__':
    sample_string = "a,, b, ,c,  ,d"
    result = split_and_filter_string(sample_string)
    print(result)