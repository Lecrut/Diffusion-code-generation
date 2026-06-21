def tokenize_string(input_str):
    return [segment for segment in input_str.replace('-', ' ').replace('_', ' ').split() if segment.isalnum()]

if __name__ == '__main__':
    sample = "hard-coded-string-with-hyphens-and_underscores"
    print(tokenize_string(sample))