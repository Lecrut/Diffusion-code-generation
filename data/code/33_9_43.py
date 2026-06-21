def minify_text(input_string):
    if not isinstance(input_string, str):
        raise ValueError('Input must be a string')
    stripped = input_string.strip()
    replaced_newlines = stripped.replace('\n', ' ')
    replaced_tabs = replaced_newlines.replace('\t', ' ')
    result = ' '.join(replaced_tabs.split())
    return result
if __name__ == '__main__':
    sample_input = '   This is a\ttest string.\nIt contains various whitespaces.  '
    minified_text = minify_text(sample_input)
    print(minified_text)