def extract_first_word(text):
    if not isinstance(text, str):
        raise ValueError('Input must be a string')
    words = text.split()
    if words:
        return words[0]
    else:
        return ''
if __name__ == '__main__':
    sample_string1 = 'This is a sample sentence'
    result1 = extract_first_word(sample_string1)
    print(result1)
    sample_string2 = '  leading spaces and multiple words'
    result2 = extract_first_word(sample_string2)
    print(result2)
    sample_string3 = 'singleword'
    result3 = extract_first_word(sample_string3)
    print(result3)
    sample_string4 = ''
    result4 = extract_first_word(sample_string4)
    print(result4)
    sample_string5 = '   '
    result5 = extract_first_word(sample_string5)
    print(result5)