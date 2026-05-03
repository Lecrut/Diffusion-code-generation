def extract_all_substrings(text, substrings):
    results = []
    for sub in substrings:
        start_index = -1
        while True:
            start_index = text.find(sub, start_index + 1)
            if start_index == -1:
                break
            results.append(start_index)
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
    sample_text_3 = "aaaaa"
    sample_substrings_3 = ["aa", "aaa"]
    found_indices_3 = extract_all_substrings(sample_text_3, sample_substrings_3)
    print(found_indices_3)