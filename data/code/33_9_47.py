def minify_text(input_string):
    if not isinstance(input_string, str):
        raise ValueError('Input must be a string')
    NEWLINE = '\n'
    TAB = '\t'
    replaced = input_string.replace(NEWLINE, ' ').replace(TAB, ' ')
    result = ''.join(replaced.split())
    return result
if __name__ == '__main__':
    sample_input = '   This is a\ttest string.\nIt contains various whitespaces.  '
    result = minify_text(sample_input)
    print(result)