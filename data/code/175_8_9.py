def tokenize_string(input_str):
    segments = input_str.replace('-', ' ').replace('_', ' ').split()
    return [segment for segment in segments if segment.isalnum()]

if __name__ == '__main__':
    sample_input = "hello-world_example_text"
    result = tokenize_string(sample_input)
    print(result)