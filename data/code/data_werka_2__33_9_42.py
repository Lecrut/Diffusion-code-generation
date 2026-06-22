def minify_text(input_string):
    if not isinstance(input_string, str):
        raise ValueError('Input must be a string')
    WHITESPACE_CHARS = {' ', '\t', '\n', '\r'}
    stripped = input_string.strip()
    result = ''.join((' ' if char in WHITESPACE_CHARS else char for char in stripped))
    minified_result = ' '.join(result.split())
    return minified_result
if __name__ == '__main__':
    sample_input = '   This is a\ttest string.\nIt contains various whitespaces.  '
    result = minify_text(sample_input)
    print(result)