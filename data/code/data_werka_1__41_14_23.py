def transform_string(s):
    upper_part = ''.join(c.upper() for c in s)
    lower_part = ''.join(c.lower() for c in s)
    return upper_part, lower_part

if __name__ == '__main__':
    sample_string = "HelloWorld"
    upper, lower = transform_string(sample_string)
    print(upper)
    print(lower)