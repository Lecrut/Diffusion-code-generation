def sort_alphabetically(strings):
    return sorted(strings, key=lambda s: s.lower())

if __name__ == '__main__':
    sample_strings = ['apple', 'Banana', 'cherry', 'date']
    sorted_strings = sort_alphabetically(sample_strings)
    print(sorted_strings)