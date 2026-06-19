def find_nested_substrings(phrase):
    if not isinstance(phrase, str):
        raise ValueError("Input must be a string")
    
    n = len(phrase)
    substrings = set()
    
    def generate_substrings(start, end):
        if start >= end:
            return
        for i in range(start + 1, end + 1):
            substrings.add(phrase[start:i])
            generate_substrings(i, end)
    
    generate_substrings(0, n)
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