def minify_text(input_string):
    if not isinstance(input_string, str):
        raise ValueError('Input must be a string')
    return ''.join(input_string.split())
if __name__ == '__main__':
    sample_input = '   This is a\ttest string.\nIt contains various whitespaces.  '
    result = minify_text(sample_input)
    print(result)