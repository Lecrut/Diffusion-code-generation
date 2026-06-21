sample_string = "  This   is a    sample string with leading, trailing, and multiple internal spaces.  "

def split_string(s):
    return s.split()

if __name__ == '__main__':
    result = split_string(sample_string)
    print(result)