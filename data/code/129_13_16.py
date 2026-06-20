def sort_strings_by_length_and_alphabet(strings):
    return sorted(strings, key=lambda s: (len(s), s))

if __name__ == '__main__':
    sample_strings = [
        "apple",
        "banana",
        "cherry",
        "date",
        "elderberry",
        "fig",
        "grape"
    ]
    print("Original Strings:")
    print(sample_strings)
    sorted_strings = sort_strings_by_length_and_alphabet(sample_strings)
    print("Sorted Strings:")
    print(sorted_strings)