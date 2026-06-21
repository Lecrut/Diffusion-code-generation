class StringAnalyzer:

    def __init__(self):
        self.total_characters = 0

    def get_length(self, text):
        if not isinstance(text, str):
            raise ValueError('Input must be a string')
        length = len(text)
        self.total_characters += length
        return length

    def get_total_characters_analyzed(self):
        return self.total_characters
if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_text1 = 'Hello, World!'
    sample_text2 = 'Python Programming'
    sample_text3 = 'Alibaba Cloud'
    print(analyzer.get_length(sample_text1))
    print(analyzer.get_length(sample_text2))
    print(analyzer.get_total_characters_analyzed())