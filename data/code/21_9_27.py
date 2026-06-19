def sort_strings_case_insensitive(strings):
    return sorted(strings, key=lambda s: s.lower())

if __name__ == '__main__':
    sample_list = ['banana', 'Apple', 'cherry', 'date', 'Elderberry']
    sorted_list = sort_strings_case_insensitive(sample_list)
    print(sorted_list)