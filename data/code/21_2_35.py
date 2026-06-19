def sort_strings_alphabetically(strings):
    return sorted(strings, key=lambda s: (s.lower(), s))

if __name__ == '__main__':
    sample_values = ["banana", "Apple", "cherry", "apple", "Banana"]
    sorted_values = sort_strings_alphabetically(sample_values)
    print(sorted_values)