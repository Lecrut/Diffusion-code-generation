def build_string_from_parts(parts, separator=''):
    if not isinstance(parts, list):
        raise ValueError('The first argument must be a list.')
    return separator.join(parts)
if __name__ == '__main__':
    sample_parts = ['Hello', 'world']
    sample_separator = ', '
    result = build_string_from_parts(sample_parts, sample_separator)
    print(result)
    empty_parts = []
    empty_result = build_string_from_parts(empty_parts, sample_separator)
    print(empty_result)
    no_separator_result = build_string_from_parts(sample_parts)
    print(no_separator_result)