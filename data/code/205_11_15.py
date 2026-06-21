def sort_strings_case_insensitive(strings):
    return sorted(strings, key=lambda s: s.lower())

if __name__ == '__main__':
    unsorted_strings = ['banana', 'Apple', 'cherry', 'date']
    sorted_strings = sort_strings_case_insensitive(unsorted_strings)
    print(sorted_strings)