def sort_strings_case_insensitive(strings):
    return sorted(strings, key=str.lower)

if __name__ == '__main__':
    sample_list = ['banana', 'Apple', 'cherry', 'date']
    sorted_list = sort_strings_case_insensitive(sample_list)
    print(sorted_list)