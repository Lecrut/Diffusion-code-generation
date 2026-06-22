def sort_strings_by_length(strings):
    return sorted(strings, key=len)

if __name__ == '__main__':
    SAMPLE_VALUES = ["apple", "banana", "pear", "kiwi", "grape"]
    SORTED_VALUES = sort_strings_by_length(SAMPLE_VALUES)
    print(SORTED_VALUES)