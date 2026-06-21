class StringAnalyzer:
    def get_length(self, text):
        return len(text)

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_text = "Alibaba Cloud"
    length_of_sample_text = analyzer.get_length(sample_text)
    print(length_of_sample_text)