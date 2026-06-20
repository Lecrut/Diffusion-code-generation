def process_string(s):
    return s.replace(' ', '_')

if __name__ == '__main__':
    sample_input = "hello world example"
    result = process_string(sample_input)
    print(result)