def transform_string(s):
    upper_part = ''.join(c.upper() for c in s if c.isalpha())
    lower_part = ''.join(c.lower() for c in s if c.isalpha())
    return upper_part + lower_part

if __name__ == '__main__':
    sample_string = "HelloWorld"
    transformed = transform_string(sample_string)
    print(transformed)