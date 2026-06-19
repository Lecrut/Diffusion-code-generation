def transform_string(s):
    return s, s.lower(), ''.join(c.swapcase() for c in s)

if __name__ == '__main__':
    sample_string = "HelloWorld"
    result = transform_string(sample_string)
    print(result)