def extract_substrings(text, indices):
    def get_substring(start, end):
        return text[start:end]

    substrings = [get_substring(start, end) for start, end in indices]
    return substrings

if __name__ == '__main__':
    sample_text = "Python is a widely-used programming language."
    sample_indices = [(0, 6), (18, 24), (35, 49), (7, 9)]
    result = extract_substrings(sample_text, sample_indices)
    print(result)