def categorize_strings_by_first_char(strings):
    categorized = {}
    for s in strings:
        if s:
            first_char = s[0].lower()
            if first_char not in categorized:
                categorized[first_char] = []
            categorized[first_char].append(s)
    return {k: sorted(v) for k, v in categorized.items()}

if __name__ == '__main__':
    sample_strings = ['apple', 'Banana', 'apricot', 'cherry', 'blueberry', 'avocado']
    result = categorize_strings_by_first_char(sample_strings)
    print(result)