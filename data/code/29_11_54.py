def reverse_string(s):
    if not isinstance(s, str):
        raise ValueError('Input must be a string')
    return s[::-1]

class StringProcessor:

    def __init__(self, text):
        self.text = text

    def process(self):
        try:
            reversed_text = reverse_string(self.text)
            return f'Original: {self.text}, Reversed: {reversed_text}'
        except ValueError as e:
            return f'Error: {e}'
if __name__ == '__main__':
    sample_texts = ['Hello, World!', 12345, 'Alibaba Cloud', 'Python Programming']
    for text in sample_texts:
        processor = StringProcessor(text)
        result = processor.process()
        print(result)