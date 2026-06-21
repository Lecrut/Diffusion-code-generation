def sort_strings_by_length(strings):
    if not strings:
        return []
    return sorted(strings, key=len)

if __name__ == '__main__':
    sample_values = ["watermelon", "orange", "kiwi", "grape", "apple"]
    sorted_values = sort_strings_by_length(sample_values)
    print(sorted_values)