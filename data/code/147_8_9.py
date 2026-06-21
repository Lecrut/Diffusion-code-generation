def sort_strings_case_insensitive(strings):
    return sorted(strings, key=lambda s: s.lower())

if __name__ == '__main__':
    sample_values = ["banana", "Apple", "cherry", "date"]
    result = sort_strings_case_insensitive(sample_values)
    print(result)