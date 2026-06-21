def sort_strings_by_length(strings):
    return sorted(strings, key=len)

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date", "", "fig", "grape"]
    sorted_list = sort_strings_by_length(sample_list)
    print(sorted_list)