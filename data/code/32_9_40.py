class StringAnalyzer:

    def __init__(self):
        self._length_cache = {}

    def get_length(self, text):
        if not isinstance(text, str):
            raise ValueError('Input must be a string')
        if text in self._length_cache:
            return self._length_cache[text]
        length = len(text)
        self._length_cache[text] = length
        return length
if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_text1 = 'Hello, World!'
    sample_text2 = 'Python Programming'
    sample_text3 = 'Alibaba Cloud'
    try:
        print(analyzer.get_length(sample_text1))
        print(analyzer.get_length(sample_text2))
        print(analyzer.get_length(sample_text3))
        print(analyzer.get_length(12345))
    except ValueError as e:
        print(e)