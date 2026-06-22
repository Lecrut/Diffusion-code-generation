def remove_spaces(text):
    if not isinstance(text, str):
        raise ValueError('Input must be a string')
    translation_table = str.maketrans('', '', ' ')
    return text.translate(translation_table)

class TextProcessor:

    def __init__(self):
        self.translation_table = str.maketrans('', '', ' ')

    def process_text(self, text):
        if not isinstance(text, str):
            raise ValueError('Input must be a string')
        return text.translate(self.translation_table)
if __name__ == '__main__':
    try:
        sample_texts = ['This is a sample text with spaces.', 'Another example without any spaces.', 'Yet another variant with multiple spaces.']
        for text in sample_texts:
            print(remove_spaces(text))
        processor = TextProcessor()
        for text in sample_texts:
            print(processor.process_text(text))
    except ValueError as e:
        print(e)