def transform_string(s):
    upper_part = ''.join(c.upper() if c.isalpha() else '' for c in s)
    lower_part = ''.join(c.lower() if c.isalpha() else '' for c in s)
    return upper_part + lower_part

if __name__ == '__main__':
    sample_string = "Python3.8"
    transformed = transform_string(sample_string)
    print(transformed)