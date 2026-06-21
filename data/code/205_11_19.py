def sort_alphabetically(strings):
    if not all(isinstance(s, str) for s in strings):
        raise ValueError("All elements must be strings")
    return sorted(strings, key=str.lower)

if __name__ == '__main__':
    sample_strings = ['banana', 'Apple', 'cherry', 'date']
    sorted_strings = sort_alphabetically(sample_strings)
    print(sorted_strings)