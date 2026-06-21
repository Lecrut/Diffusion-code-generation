def categorize_strings_by_first_char(strings):
    categorized = {}
    for string in strings:
        if not isinstance(string, str) or len(string) == 0:
            raise ValueError("All items must be non-empty strings.")
        first_char = string[0]
        if first_char not in categorized:
            categorized[first_char] = []
        categorized[first_char].append(string)
    return {k: sorted(v) for k, v in categorized.items()}

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "avocado", "apricot", "blueberry"]
    print(categorize_strings_by_first_char(sample_strings))