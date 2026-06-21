def tokenize_string(s):
    return [segment for segment in s.replace('-', ' ').replace('_', ' ').split() if segment.isalnum()]

if __name__ == '__main__':
    sample_string = "hello-world_this-is_a-test"
    print(tokenize_string(sample_string))