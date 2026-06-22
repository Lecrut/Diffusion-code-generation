def minify_text(input_string):
    if not isinstance(input_string, str):
        raise ValueError('Input must be a string')
    stripped = input_string.strip()
    replaced_newlines = stripped.replace('\n', ' ')
    replaced_tabs = replaced_newlines.replace('\t', ' ')
    words = replaced_tabs.split()
    minified_text = ' '.join(words)
    return minified_text
if __name__ == '__main__':
    sample_input = '   Another example \nwith different \twhitespaces.  '
    result = minify_text(sample_input)
    print(result)