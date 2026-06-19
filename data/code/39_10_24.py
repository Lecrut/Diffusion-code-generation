def extract_substrings(text, indices):
    def validate_indices(text_length, start, end):
        if not (0 <= start < text_length and 0 <= end <= text_length and start <= end):
            raise ValueError(f"Invalid indices: ({start}, {end}) for text length {text_length}")

    substrings = []
    text_length = len(text)
    for start, end in indices:
        validate_indices(text_length, start, end)
        substrings.append(text[start:end])
    return substrings

if __name__ == '__main__':
    sample_text = "This is a sample string for testing purposes."
    sample_indices = [(0, 4), (10, 15), (30, 40), (5, 5)]
    try:
        result = extract_substrings(sample_text, sample_indices)
        print(result)
    except ValueError as e:
        print(e)