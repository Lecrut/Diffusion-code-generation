def extract_substrings(text, indices):
    substrings = []
    for start, end in indices:
        if not isinstance(start, int) or not isinstance(end, int):
            raise ValueError("Both start and end indices must be integers.")
        if start < 0 or end > len(text) or start > end:
            raise ValueError(f"Invalid index range: ({start}, {end})")
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