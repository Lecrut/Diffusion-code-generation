def replace_whitespace_with_underscores(text):
    return text.replace(' ', '_').replace('\t', '_').replace('\n', '_').replace('\r', '_')

if __name__ == '__main__':
    sample_text = "Hello   World\nNew\tTab"
    result = replace_whitespace_with_underscores(sample_text)
    print(result)