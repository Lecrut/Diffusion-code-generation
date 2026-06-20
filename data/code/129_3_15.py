def sort_strings_by_length_and_alphabet(strings):
    return sorted(strings, key=lambda s: (-len(s), s))

if __name__ == '__main__':
    sample_values = ["apple", "banana", "cherry", "date", "elderberry"]
    sorted_list = sort_strings_by_length_and_alphabet(sample_values)
    print(sorted_list)