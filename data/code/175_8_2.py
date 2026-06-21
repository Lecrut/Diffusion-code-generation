def tokenize_string(input_str):
    return [segment for segment in input_str.replace('-', ' ').replace('_', ' ').split() if segment.isalnum()]

if __name__ == '__main__':
    sample_str = "hello-world_example"
    print(tokenize_string(sample_str))