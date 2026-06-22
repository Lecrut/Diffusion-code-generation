def sort_strings(strings):
    return sorted(strings, key=lambda s: s.lower())

if __name__ == '__main__':
    sample_strings = ["banana", "Apple", "cherry", "date", "Elderberry"]
    sorted_list = sort_strings(sample_strings)
    print(sorted_list)