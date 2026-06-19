def sort_strings_by_length(strings):
    return sorted(strings, key=len)

if __name__ == '__main__':
    sample_list = ["apple", "banana", "pear", "kiwi", "grape"]
    empty_list = []
    identical_length_list = ["dog", "cat", "bat"]

    print("Sorted by length:", sort_strings_by_length(sample_list))
    print("Empty list sorted:", sort_strings_by_length(empty_list))
    print("Identical length sorted:", sort_strings_by_length(identical_length_list))