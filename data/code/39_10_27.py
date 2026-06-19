def extract_substrings(text, indices):
    return [text[start:end] for start, end in indices]

if __name__ == '__main__':
    sample_text = "Extracting substrings efficiently."
    sample_indices = [(0, 8), (10, 23), (25, 35), (5, 7)]
    result = extract_substrings(sample_text, sample_indices)
    print(result)