def sort_strings_by_length_and_alphabet(strings):
    return sorted(strings, key=lambda s: (len(s), s))

if __name__ == '__main__':
    sample_values = ["banana", "apple", "cherry", "date", "elderberry"]
    print(sort_strings_by_length_and_alphabet(sample_values))