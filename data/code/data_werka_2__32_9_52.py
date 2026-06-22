class StringAnalyzer:
    def get_length(self, text):
        if not isinstance(text, str):
            raise ValueError('Input must be a string')
        length = len(text)
        return length

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_text1 = "OpenAI"
    sample_text2 = "GPT-4"
    try:
        print(analyzer.get_length(sample_text1))
        print(analyzer.get_length(sample_text2))
    except ValueError as e:
        print(e)