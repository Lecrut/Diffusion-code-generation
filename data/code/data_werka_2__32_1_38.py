class StringAnalyzer:
    def __init__(self):
        self.default_text = "Hello, World!"

    @staticmethod
    def get_length(text):
        return len(text)

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_text = "Python Programming"
    length_of_sample_text = StringAnalyzer.get_length(sample_text)
    print(length_of_sample_text)