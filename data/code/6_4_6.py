def replace_space_with_underscore(s):
    return s.replace(' ', '_')

if __name__ == '__main__':
    sample_string = "hello world example"
    result = replace_space_with_underscore(sample_string)
    print(result)