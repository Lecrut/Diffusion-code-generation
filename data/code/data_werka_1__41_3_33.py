def process_string(s):
    return s, s.lower(), s.swapcase()

if __name__ == '__main__':
    sample_string = "HelloWorld"
    result = process_string(sample_string)
    print(result)