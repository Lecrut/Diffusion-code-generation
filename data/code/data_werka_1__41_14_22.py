def transform_string(s):
    upper_part = ''.join(c for c in s if c.isupper())
    lower_part = ''.join(c for c in s if c.islower())
    return upper_part + lower_part

if __name__ == '__main__':
    sample_string = "HelloWorld"
    transformed = transform_string(sample_string)
    print(transformed)