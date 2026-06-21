def format_to_integers(text):
    formatting_chars = ''.join((chr(i) for i in range(32, 128) if not chr(i).isdigit() and chr(i) != '-'))
    translation_table = str.maketrans('', '', formatting_chars)
    cleaned_text = text.translate(translation_table)
    if not cleaned_text:
        return ''
    tokens = cleaned_text.split()
    integers = []
    for token in tokens:
        try:
            int(token)
            integers.append(token)
        except ValueError:
            raise ValueError('The remaining string does not consist solely of integers.')
    result = ' '.join(integers)
    return result
if __name__ == '__main__':
    sample_text = '  123  456.789  -10  +20  abc  300  400.5  '
    result = format_to_integers(sample_text)
    print(result)