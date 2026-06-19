class StringAnalyzer:
    def get_length(self, text):
        return len(text)

if __name__ == '__main__':
    SAMPLE_TEXT_1 = "Hello World"
    SAMPLE_TEXT_2 = "Python Programming"
    SAMPLE_TEXT_3 = ""
    SAMPLE_TEXT_4 = "a"

    analyzer = StringAnalyzer()
    
    print(analyzer.get_length(SAMPLE_TEXT_1))
    print(analyzer.get_length(SAMPLE_TEXT_2))
    print(analyzer.get_length(SAMPLE_TEXT_3))
    print(analyzer.get_length(SAMPLE_TEXT_4))