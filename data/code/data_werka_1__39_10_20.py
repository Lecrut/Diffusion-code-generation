def extract_substrings(s, indices):
    return [s[start:end] for start, end in indices]

if __name__ == '__main__':
    sample_string = "Hello, World!"
    sample_indices = [(0, 5), (7, 12)]
    result = extract_substrings(sample_string, sample_indices)
    print(result)