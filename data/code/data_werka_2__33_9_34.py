def minify_text(input_string):
    stripped = input_string.strip()
    no_newlines = stripped.replace('\n', ' ')
    no_tabs = no_newlines.replace('\t', ' ')
    single_spaces = ' '.join(no_tabs.split())
    return single_spaces

if __name__ == '__main__':
    sample_input = "   This is a\ttest string.\nIt contains various whitespaces.  "
    result = minify_text(sample_input)
    print(result)