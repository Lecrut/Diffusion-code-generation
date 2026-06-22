def minify_text(input_string):
    if not isinstance(input_string, str):
        raise ValueError('Input must be a string')
    stripped = input_string.strip()
    replaced = stripped.replace('\n', ' ').replace('\t', ' ')
    result = ' '.join(replaced.split())
    return result
if __name__ == '__main__':
    sample_input = '   This is a\ttest string.\nIt contains various whitespaces.  '
    result = minify_text(sample_input)
    print(result)