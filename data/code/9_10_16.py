def strip_whitespace(text):
    return text.strip()
if __name__ == '__main__':
    sample_inputs = ['  hello world  ', '\t\nPython is awesome\n\t', '   ', '', 'no_whitespace', '  mixed\t\nspaces  ']
    for sample in sample_inputs:
        result = strip_whitespace(sample)
        print(repr(result))