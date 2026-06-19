def extract_all_substrings(text, substrings):
    if not isinstance(text, str):
        raise ValueError("The text must be a string.")
    if not isinstance(substrings, list) or not all(isinstance(s, str) for s in substrings):
        raise ValueError("Substrings must be provided as a list of strings.")
    
    results = []
    for sub in substrings:
        start_index = -1
        while True:
            try:
                start_index = text.index(sub, start_index + 1)
                results.append(start_index)
            except ValueError:
                break
    return results

if __name__ == '__main__':
    sample_text = "abababa"
    sample_substrings = ["aba", "ab", "ba"]
    found_indices = extract_all_substrings(sample_text, sample_substrings)
    print(found_indices)

    sample_text_2 = "banana"
    sample_substrings_2 = ["ana", "na"]
    found_indices_2 = extract_all_substrings(sample_text_2, sample_substrings_2)
    print(found_indices_2)