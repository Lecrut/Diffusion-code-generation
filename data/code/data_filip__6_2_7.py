def replace_whitespace_with_underscore(text):
    return text.replace(' ', '_').replace('\t', '_').replace('\n', '_').replace('\r', '_').replace('\f', '_').replace('\v', '_')

if __name__ == '__main__':
    sample_text = "Hello   World\tNew\nLine"
    result = replace_whitespace_with_underscore(sample_text)
    print(result)