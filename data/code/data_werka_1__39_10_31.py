def extract_substrings(text, indices):
    def validate_indices(start, end):
        if not (0 <= start < len(text) and 0 <= end <= len(text)):
            raise ValueError(f"Invalid index range: ({start}, {end})")
        if start > end:
            raise ValueError(f"Start index must be less than or equal to end index: ({start}, {end})")

    substrings = []
    for start, end in indices:
        validate_indices(start, end)
        substrings.append(text[start:end])
    return substrings

if __name__ == '__main__':
    sample_text = "This is a sample string for testing purposes."
    sample_indices = [(0, 4), (10, 15), (30, 40), (5, 7)]
    try:
        result = extract_substrings(sample_text, sample_indices)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")