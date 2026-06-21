def sort_strings_by_length(strings):
    return sorted(strings, key=len)

if __name__ == '__main__':
    sample_list = ["apple", "banana", "pear", "kiwi", "grape"]
    print(sort_strings_by_length(sample_list))