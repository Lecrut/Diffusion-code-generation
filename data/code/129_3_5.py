def sort_strings_by_length_and_alphabet(strings):
    return sorted(strings, key=lambda x: (-len(x), x))

if __name__ == '__main__':
    sample_values = ["apple", "banana", "cherry", "date", "elderberry"]
    print(sort_strings_by_length_and_alphabet(sample_values))