def sort_alphabetically(strings):
    return sorted(strings, key=lambda s: s.lower())

if __name__ == '__main__':
    sample_strings = ['banana', 'Apple', 'cherry', 'date']
    print(sort_alphabetically(sample_strings))