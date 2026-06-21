def tokenize_string(input_str):
    replacements = {'-': ' ', '_': ' '}
    for char, replacement in replacements.items():
        input_str = input_str.replace(char, replacement)
    return [segment for segment in input_str.split() if segment.isalnum()]

if __name__ == '__main__':
    sample_str = "hello-world_example-text"
    print(tokenize_string(sample_str))