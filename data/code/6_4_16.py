def transform_string(s):
    return s.replace(' ', '_')

if __name__ == '__main__':
    sample_input = "hello world example"
    print(transform_string(sample_input))