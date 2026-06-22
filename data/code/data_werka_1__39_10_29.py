def extract_substrings(s, indices):
    substrings = []
    for start, end in indices:
        if 0 <= start < end <= len(s):
            substrings.append(s[start:end])
        else:
            substrings.append(None)
    return substrings

if __name__ == '__main__':
    sample_string = "Hello, World!"
    sample_indices = [(0, 5), (7, 12), (13, 20), (-1, 5), (0, 20)]
    result = extract_substrings(sample_string, sample_indices)
    print(result)