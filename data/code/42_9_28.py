def build_string_from_parts(parts, separator=''):
    if not parts:
        return ''
    return separator.join(parts)
if __name__ == '__main__':
    sample_parts = ['Hello', 'world']
    sample_separator = ', '
    result = build_string_from_parts(sample_parts, sample_separator)
    print(result)