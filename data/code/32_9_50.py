class StringAnalyzer:
    MAX_LENGTH = 1000

    def __init__(self):
        self.length_cache = {}

    @staticmethod
    def _validate_input(text):
        if not isinstance(text, str):
            raise ValueError('Input must be a string')
        if len(text) > StringAnalyzer.MAX_LENGTH:
            raise ValueError(f'Input text exceeds maximum length of {StringAnalyzer.MAX_LENGTH}')

    def get_length(self, text):
        self._validate_input(text)
        if text in self.length_cache:
            return self.length_cache[text]
        else:
            length = len(text)
            self.length_cache[text] = length
            return length

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_text1 = "Hello, World!"
    sample_text2 = "Python Programming"
    print(analyzer.get_length(sample_text1))
    print(analyzer.get_length(sample_text2))