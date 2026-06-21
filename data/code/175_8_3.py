def tokenize_string(input_string):
    return [segment for segment in input_string.replace('-', ' ').replace('_', ' ').split() if segment.isalnum()]

if __name__ == '__main__':
    sample_string = "hello-world_this-is-a-test"
    print(tokenize_string(sample_string))