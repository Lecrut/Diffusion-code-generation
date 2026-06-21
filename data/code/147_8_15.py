def sort_strings_case_insensitive(strings):
    if not all(isinstance(s, str) for s in strings):
        raise ValueError("All elements must be strings")
    return sorted(strings, key=lambda s: s.lower())

if __name__ == '__main__':
    sample_values = ["banana", "Apple", "cherry", "date"]
    print(sort_strings_case_insensitive(sample_values))