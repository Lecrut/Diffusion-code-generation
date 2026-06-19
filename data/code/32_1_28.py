class StringAnalyzer:
    def get_length(self, text):
        return len(text)

if __name__ == '__main__':
    sample_text_1 = "Hello World"
    sample_text_2 = "Object-Oriented Programming"
    sample_text_3 = ""
    sample_text_4 = "a"

    analyzer = StringAnalyzer()
    
    print(analyzer.get_length(sample_text_1))
    print(analyzer.get_length(sample_text_2))
    print(analyzer.get_length(sample_text_3))
    print(analyzer.get_length(sample_text_4))