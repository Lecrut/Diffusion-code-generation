class StringAnalyzer:
    def get_length(self, text):
        return len(text)

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_text_1 = "Welcome to Alibaba Cloud"
    sample_text_2 = "Qwen AI Model"
    sample_text_3 = ""
    sample_text_4 = "a"

    length_1 = analyzer.get_length(sample_text_1)
    length_2 = analyzer.get_length(sample_text_2)
    length_3 = analyzer.get_length(sample_text_3)
    length_4 = analyzer.get_length(sample_text_4)

    print(length_1)
    print(length_2)
    print(length_3)
    print(length_4)