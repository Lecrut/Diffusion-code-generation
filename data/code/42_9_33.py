def build_string_from_parts(parts, separator=None):
    if not parts:
        return ''
    if separator is None:
        return ''.join(parts)
    return separator.join(parts)
if __name__ == '__main__':
    sample_parts_1 = ['apple', 'banana', 'cherry']
    sample_separator_1 = ','
    result_1 = build_string_from_parts(sample_parts_1, sample_separator_1)
    print(f"Parts: {sample_parts_1}, Separator: '{sample_separator_1}' -> Result: '{result_1}'")
    sample_parts_2 = ['hello', 'world']
    sample_separator_2 = ' '
    result_2 = build_string_from_parts(sample_parts_2, sample_separator_2)
    print(f"Parts: {sample_parts_2}, Separator: '{sample_separator_2}' -> Result: '{result_2}'")
    sample_parts_3 = ['one', 'two', 'three']
    sample_separator_3 = ''
    result_3 = build_string_from_parts(sample_parts_3, sample_separator_3)
    print(f"Parts: {sample_parts_3}, Separator: '{sample_separator_3}' -> Result: '{result_3}'")
    sample_parts_4 = []
    sample_separator_4 = ','
    result_4 = build_string_from_parts(sample_parts_4, sample_separator_4)
    print(f"Parts: {sample_parts_4}, Separator: '{sample_separator_4}' -> Result: '{result_4}'")
    sample_parts_5 = ['alpha', 'beta', 'gamma']
    result_5 = build_string_from_parts(sample_parts_5, None)
    print(f"Parts: {sample_parts_5}, Separator: None -> Result: '{result_5}'")