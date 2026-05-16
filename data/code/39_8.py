def find_matching_substrings(text, patterns):
    results = {}
    for pattern in patterns:
        matches = []
        for i in range(len(text) - len(pattern) + 1):
            substring = text[i:i + len(pattern)]
            if substring == pattern:
                matches.append(substring)
        results[pattern] = matches
    return results
if __name__ == '__main__':
    sample_text = "abababa"
    sample_patterns = ["aba", "bab", "a", "b"]
    output = find_matching_substrings(sample_text, sample_patterns)
    print(output)