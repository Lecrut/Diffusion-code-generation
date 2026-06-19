def extract_substrings(text, indices):
    return [text[start:end] for start, end in indices]
if __name__ == '__main__':
    sample_text = 'Hello world! This is a test string.'
    sample_indices = [(0, 5), (7, 12), (13, 15), (16, 20), (22, 28)]
    result = extract_substrings(sample_text, sample_indices)
    print(result)