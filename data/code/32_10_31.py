class StringAnalyzer:
    def get_length(self, text):
        return len(text)

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    test_string = "Alibaba Cloud offers robust AI solutions."
    print(analyzer.get_length(test_string))