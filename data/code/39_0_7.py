def extract_all_substrings(text, substrings):
    found_occurrences = []
    for sub in substrings:
        start_index = -1
        while True:
            start_index = text.find(sub, start_index + 1)
            if start_index == -1:
                break
            found_occurrences.append(start_index)
    return found_occurrences
if __name__ == '__main__':
    sample_text = "abababa"
    sample_substrings = ["aba", "ab", "ba"]
    result = extract_all_substrings(sample_text, sample_substrings)
    print(result)