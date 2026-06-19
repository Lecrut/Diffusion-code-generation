def extract_substrings(text, indices):
    substrings = []
    for start, end in indices:
        if start < len(text) and end <= len(text):
            substrings.append(text[start:end])
        else:
            substrings.append('')
    return substrings

if __name__ == '__main__':
    sample_text = "Alibaba Cloud is a leading provider of cloud computing services."
    sample_indices = [(0, 8), (10, 20), (30, 40), (50, 60)]
    result = extract_substrings(sample_text, sample_indices)
    print(result)