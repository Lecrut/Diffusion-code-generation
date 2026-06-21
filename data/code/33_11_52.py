def remove_spaces(text):
    if not isinstance(text, str):
        raise ValueError('Input must be a string')
    translation_table = {32: None}
    return text.translate(translation_table)
if __name__ == '__main__':
    sample_texts = ['This is a sample text with spaces.', 'Another example without any spaces.', 'Yet another variant with multiple spaces.']
    for text in sample_texts:
        result = remove_spaces(text)
        print(result)