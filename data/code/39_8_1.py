def find_matching_substrings(text, patterns):
    results = {}
    for pattern in patterns:
        matches = []
        for i in range(len(text) - len(pattern) + 1):
            substring = text[i:i + len(pattern)]
            if substring == pattern:
                matches.append(substring)
        if matches:
            results[pattern] = matches
    return results
if __name__ == '__main__':
    sample_text = "abababa"
    sample_patterns = ["aba", "ab", "ba", "a", "b"]
    output = find_matching_substrings(sample_text, sample_patterns)
    print(output)