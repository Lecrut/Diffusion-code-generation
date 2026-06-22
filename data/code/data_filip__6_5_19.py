def replace_spaces_with_underscores(s):
    return s.replace(' ', '_')

if __name__ == '__main__':
    sample_string = "hello world this is a test"
    result = replace_spaces_with_underscores(sample_string)
    print(result)