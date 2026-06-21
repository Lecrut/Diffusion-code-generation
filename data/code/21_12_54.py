def sort_strings_by_length(strings):
    if not strings:
        return []
    sorted_list = sorted(strings, key=len)
    return sorted_list
if __name__ == '__main__':
    sample_values = ['strawberry', 'blueberry', 'raspberry', 'blackberry', 'a']
    sorted_values = sort_strings_by_length(sample_values)
    print(sorted_values)