def string_transformations(s):
    return (s, s.lower(), s.swapcase())

if __name__ == '__main__':
    sample_string = "HelloWorld"
    result = string_transformations(sample_string)
    print(result)