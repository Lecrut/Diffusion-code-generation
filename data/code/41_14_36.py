def transform_string(s):
    UPPER_CASE_THRESHOLD = ord('Z')
    LOWER_CASE_THRESHOLD = ord('z')

    upper_part = []
    lower_part = []

    for char in s:
        if ord(char) <= UPPER_CASE_THRESHOLD and ord(char) >= ord('A'):
            upper_part.append(char)
        elif ord(char) <= LOWER_CASE_THRESHOLD and ord(char) >= ord('a'):
            lower_part.append(char)

    return ''.join(upper_part + lower_part)

if __name__ == '__main__':
    sample_string = "HelloWorld"
    transformed = transform_string(sample_string)
    print(transformed)