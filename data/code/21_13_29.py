def sort_strings_by_length(strings):
    return sorted(strings, key=len)

if __name__ == '__main__':
    sample_values = ["apple", "banana", "pear", "", "kiwi", "grape"]
    sorted_list = sort_strings_by_length(sample_values)
    print(sorted_list)