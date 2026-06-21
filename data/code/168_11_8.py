def categorize_strings_by_first_char(strings):
    categorized = {}
    for s in strings:
        if s[0] not in categorized:
            categorized[s[0]] = []
        categorized[s[0]].append(s)
    return {k: sorted(v) for k, v in categorized.items()}

if __name__ == '__main__':
    sample_strings = ['apple', 'banana', 'apricot', 'cherry', 'blueberry']
    result = categorize_strings_by_first_char(sample_strings)
    print(result)