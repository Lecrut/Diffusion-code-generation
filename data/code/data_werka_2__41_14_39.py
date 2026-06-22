def transform_string(s):
    upper_part = ''.join([char.upper() if char.islower() else char for char in s])
    lower_part = ''.join([char.lower() if char.isupper() else char for char in s])
    return upper_part, lower_part

if __name__ == '__main__':
    sample_string = "HelloWorld"
    upper_str, lower_str = transform_string(sample_string)
    print(upper_str)
    print(lower_str)