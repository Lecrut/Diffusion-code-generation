def sort_alphabetically(string_list):
    return sorted(string_list, key=lambda s: s.lower())

if __name__ == '__main__':
    sample_values = ["banana", "Apple", "cherry", "date"]
    print(sort_alphabetically(sample_values))