def sort_strings_by_length(strings):
    if not strings:
        return []
    length_tuples = [(len(s), s) for s in strings]
    sorted_length_tuples = sorted(length_tuples)
    sorted_strings = [s for _, s in sorted_length_tuples]
    return sorted_strings
if __name__ == '__main__':
    sample_input = ['strawberry', 'blueberry', 'raspberry', 'blackberry', 'a']
    sorted_result = sort_strings_by_length(sample_input)
    print(sorted_result)