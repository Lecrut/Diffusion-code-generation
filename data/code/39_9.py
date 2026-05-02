def find_nested_substrings(phrase):
    n = len(phrase)
    substrings = set()
    for i in range(n):
        for j in range(i + 1, n + 1):
            substrings.add(phrase[i:j])
    result = list(substrings)
    result.sort(key=lambda x: (len(x), x))
    return result
if __name__ == '__main__':
    sample_phrase = "abcabc"
    nested_substrings = find_nested_substrings(sample_phrase)
    print(nested_substrings)
    sample_phrase_2 = "banana"
    nested_substrings_2 = find_nested_substrings(sample_phrase_2)
    print(nested_substrings_2)
    sample_phrase_3 = "aaaa"
    nested_substrings_3 = find_nested_substrings(sample_phrase_3)
    print(nested_substrings_3)