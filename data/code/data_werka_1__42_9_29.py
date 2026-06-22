def build_string_from_parts(parts, separator=None):
    if not isinstance(parts, list):
        raise TypeError('Parts must be a list of strings.')
    if not all((isinstance(part, str) for part in parts)):
        raise ValueError('All elements in parts must be strings.')
    if not parts:
        return ''
    if separator is None:
        return ''.join(parts)
    return separator.join(parts)
if __name__ == '__main__':
    try:
        parts1 = ['apple', 'banana', 'cherry']
        sep1 = ','
        result1 = build_string_from_parts(parts1, sep1)
        print(f"Parts: {parts1}, Separator: '{sep1}' -> Result: '{result1}'")
        parts2 = ['Hello', 'world']
        sep2 = ' '
        result2 = build_string_from_parts(parts2, sep2)
        print(f"Parts: {parts2}, Separator: '{sep2}' -> Result: '{result2}'")
        parts3 = ['one', 'two', 'three']
        sep3 = ''
        result3 = build_string_from_parts(parts3, sep3)
        print(f"Parts: {parts3}, Separator: '{sep3}' -> Result: '{result3}'")
        parts4 = []
        result4 = build_string_from_parts(parts4, ',')
        print(f"Parts: {parts4}, Separator: ',' -> Result: '{result4}'")
        parts5 = ['a', 'b', 'c']
        result5 = build_string_from_parts(parts5, None)
        print(f"Parts: {parts5}, Separator: None -> Result: '{result5}'")
    except (TypeError, ValueError) as e:
        print(f'Error: {e}')