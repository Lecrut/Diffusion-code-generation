def tokenize_string(input_string):
    return [segment for segment in input_string.replace('-', ' ').replace('_', ' ').split() if segment.isalnum()]

if __name__ == '__main__':
    sample_string = "example-string_with-hyphens_and_underscores"
    print(tokenize_string(sample_string))