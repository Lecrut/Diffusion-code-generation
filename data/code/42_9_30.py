def build_string_from_parts(parts, separator=''):
    if not parts:
        return ''
    return separator.join(parts)
if __name__ == '__main__':
    sample_parts = ['Hello', 'world', 'this', 'is', 'a', 'test']
    sample_separator = ', '
    result = build_string_from_parts(sample_parts, sample_separator)
    print(result)
    empty_parts = []
    result_empty = build_string_from_parts(empty_parts, sample_separator)
    print(result_empty)
    single_part = ['Single']
    result_single = build_string_from_parts(single_part, sample_separator)
    print(result_single)