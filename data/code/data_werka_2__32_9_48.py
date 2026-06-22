class StringAnalyzer:
    def __init__(self):
        self.total_calls = 0

    def get_length(self, text):
        if not isinstance(text, str):
            raise ValueError('Input must be a string')
        length = len(text)
        self.total_calls += 1
        return length

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_text1 = "Alibaba Cloud"
    sample_text2 = "Python Programming"
    
    result1 = analyzer.get_length(sample_text1)
    result2 = analyzer.get_length(sample_text2)
    
    print(f"Length of '{sample_text1}': {result1}")
    print(f"Length of '{sample_text2}': {result2}")
    print(f"Total calls made to get_length: {analyzer.total_calls}")