def sort_strings(strings):
    return sorted(strings, key=lambda s: (s.lower(), s))

if __name__ == '__main__':
    sample_list = ['banana', 'Apple', 'cherry', 'date', 'Elderberry']
    sorted_list = sort_strings(sample_list)
    print(sorted_list)