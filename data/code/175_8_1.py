def tokenize_string(input_str):
    return [segment for segment in input_str.replace('-', ' ').replace('_', ' ').split() if segment.isalnum()]

if __name__ == '__main__':
    sample = "hello-world_example-text"
    print(tokenize_string(sample))