def build_string_from_parts(parts, separator=''):
    if not isinstance(parts, list):
        raise ValueError('The first argument must be a list.')
    if not all((isinstance(part, str) for part in parts)):
        raise ValueError('All elements of the list must be strings.')
    return separator.join(parts)
if __name__ == '__main__':
    sample_parts = ['Hello', 'world', 'from', 'Python']
    sample_separator = ', '
    result = build_string_from_parts(sample_parts, sample_separator)
    print(result)
    empty_list_result = build_string_from_parts([])
    print(empty_list_result)
    no_separator_result = build_string_from_parts(['a', 'b', 'c'])
    print(no_separator_result)