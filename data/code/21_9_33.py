def sort_strings(strings):
    return sorted(strings, key=lambda s: s.lower())

if __name__ == '__main__':
    sample_values = ["banana", "Apple", "cherry", "date", "Elderberry"]
    sorted_values = sort_strings(sample_values)
    print(sorted_values)