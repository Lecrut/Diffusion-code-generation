class StringAnalyzer:
    def __init__(self):
        self.text_lengths = {}

    def get_length(self, text):
        if not isinstance(text, str):
            raise ValueError('Input must be a string')
        
        if text in self.text_lengths:
            return self.text_lengths[text]
        
        length = len(text)
        self.text_lengths[text] = length
        return length

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_text1 = "Hello, World!"
    sample_text2 = "Python Programming"
    sample_text3 = "Alibaba Cloud"
    
    print(analyzer.get_length(sample_text1))
    print(analyzer.get_length(sample_text2))
    print(analyzer.get_length(sample_text3))