def tokenize_string(input_str):
    segments = input_str.replace('-', ' ').replace('_', ' ').split()
    return [segment for segment in segments if segment.isalnum()]
if __name__ == '__main__':
    sample_value = 'hello-world_example-text'
    print(tokenize_string(sample_value))