def extract_substrings(text, indices):
    return [text[start:end] for start, end in indices]

if __name__ == '__main__':
    SAMPLE_TEXT = "This is a sample string for testing purposes."
    SAMPLE_INDICES = [(0, 4), (10, 15), (30, 40), (5, 7)]
    result = extract_substrings(SAMPLE_TEXT, SAMPLE_INDICES)
    print(result)

    ANOTHER_SAMPLE_INDICES = [(0, 8), (20, 25), (35, 45), (6, 10)]
    another_result = extract_substrings(SAMPLE_TEXT, ANOTHER_SAMPLE_INDICES)
    print(another_result)