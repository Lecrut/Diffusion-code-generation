def extract_substrings(phrase, indices):
    extracted_substrings = []
    for index in indices:
        if 0 <= index < len(phrase):
            start = index
            end = index + 1
            if end <= len(phrase):
                substring = phrase[start:end]
                extracted_substrings.append(substring)
        else:
            print(f"Error: Invalid index {index}. Index must be within the bounds of the phrase (0 to {len(phrase) - 1}).")
    return extracted_substrings
if __name__ == '__main__':
    sample_phrase = "Hello World"
    sample_indices = [0, 5, 10, -1, 6]
    results = extract_substrings(sample_phrase, sample_indices)
    for sub in results:
        print(sub)