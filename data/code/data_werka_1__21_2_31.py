def sort_strings(strings):
    return sorted(strings, key=lambda s: (s.lower(), s))

if __name__ == '__main__':
    sample_strings = ['banana', 'Apple', 'cherry', 'date', 'Elderberry']
    sorted_strings = sort_strings(sample_strings)
    print(sorted_strings)