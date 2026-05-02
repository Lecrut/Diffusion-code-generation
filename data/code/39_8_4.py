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
    input_string = "abababa"
    patterns_list = ["aba", "ab", "ba", "a"]
    output = find_matching_substrings(input_string, patterns_list)
    print(output)