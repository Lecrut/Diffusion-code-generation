def sort_strings_case_insensitive(strings):
    return sorted(strings, key=lambda s: s.lower())

if __name__ == '__main__':
    sample_strings = ["banana", "Apple", "cherry", "date", "Elderberry"]
    sorted_strings = sort_strings_case_insensitive(sample_strings)
    print(sorted_strings)