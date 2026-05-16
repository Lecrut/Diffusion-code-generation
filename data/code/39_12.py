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
            print(f"Error: Invalid index {index}. Index must be within the bounds of the phrase.")
    return extracted_substrings
if __name__ == '__main__':
    sample_phrase = "HelloWorld"
    sample_indices = [0, 5, 10, -1, 3]
    print(f"Phrase: {sample_phrase}")
    print(f"Indices to check: {sample_indices}")
    results = extract_substrings(sample_phrase, sample_indices)
    print("\nExtracted Substrings:")
    for sub in results:
        print(sub)