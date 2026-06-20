def sort_by_length_and_alphabet(strings):
    return sorted(strings, key=lambda s: (len(s), s))

if __name__ == '__main__':
    sample_values = [
        "apple", "banana", "cherry", "date", 
        "elderberry", "fig", "grape"
    ]
    print("Original List:")
    print(sample_values)
    sorted_values = sort_by_length_and_alphabet(sample_values)
    print("Sorted List:")
    print(sorted_values)