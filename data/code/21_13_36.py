def sort_strings_by_length(strings):
    return sorted(strings, key=len)

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "", "date", "fig", "grape"]
    sorted_strings = sort_strings_by_length(sample_strings)
    print(sorted_strings)