def extract_all_substrings(text, substrings):
    found_occurrences = []
    for sub in substrings:
        start_index = 0
        while True:
            index = text.find(sub, start_index)
            if index == -1:
                break
            found_occurrences.append(index)
            start_index = index + 1
    return found_occurrences
if __name__ == '__main__':
    sample_text = "abababa"
    sample_substrings = ["aba", "b"]
    result = extract_all_substrings(sample_text, sample_substrings)
    print(result)
    sample_text_2 = "banana"
    sample_substrings_2 = ["an", "na"]
    result_2 = extract_all_substrings(sample_text_2, sample_substrings_2)
    print(result_2)
    sample_text_3 = "aaaaa"
    sample_substrings_3 = ["aa", "aaa"]
    result_3 = extract_all_substrings(sample_text_3, sample_substrings_3)
    print(result_3)