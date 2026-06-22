def extract_substrings(text, indices):

    def is_valid_index(start, end, length):
        return 0 <= start <= end <= length
    substrings = []
    for start, end in indices:
        if is_valid_index(start, end, len(text)):
            substrings.append(text[start:end])
        else:
            substrings.append(None)
    return substrings
if __name__ == '__main__':
    sample_text = 'This is a sample string for testing purposes.'
    sample_indices = [(0, 4), (10, 15), (30, 40), (5, 7), (-1, 5), (10, 100)]
    result = extract_substrings(sample_text, sample_indices)
    print(result)