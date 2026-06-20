def sort_strings_by_length(strings):
    return sorted(strings, key=lambda s: (len(s), s))

if __name__ == '__main__':
    sample_values = [
        "apple", "banana", "cherry", "date", "elderberry"
    ]
    print("Original Values:")
    print(sample_values)
    print("\nSorted Values:")
    print(sort_strings_by_length(sample_values))