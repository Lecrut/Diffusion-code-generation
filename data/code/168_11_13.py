def categorize_strings_by_first_char(strings):
    categorized = {}
    for s in strings:
        if s:
            first_char = s[0].lower()
            if first_char not in categorized:
                categorized[first_char] = []
            categorized[first_char].append(s)
    return {k: sorted(v) for k, v in sorted(categorized.items())}

if __name__ == '__main__':
    sample_strings = ['apple', 'Banana', 'cherry', 'date', 'Apple', 'banana']
    result = categorize_strings_by_first_char(sample_strings)
    print(result)