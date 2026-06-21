def categorize_strings(strings):
    categorized = {}
    for string in strings:
        first_char = string[0].upper()
        if first_char not in categorized:
            categorized[first_char] = []
        categorized[first_char].append(string)
    return dict(sorted(categorized.items()))

if __name__ == '__main__':
    sample_strings = ['apple', 'banana', 'apricot', 'blueberry', 'avocado']
    print(categorize_strings(sample_strings))