class StringAnalyzer:
    def get_length(self, text):
        return len(text)

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_text = "Python is great for data analysis!"
    print(analyzer.get_length(sample_text))