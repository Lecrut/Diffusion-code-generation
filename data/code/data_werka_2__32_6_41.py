class TextAnalyzer:
    @staticmethod
    def compute_length(text):
        return len(text)

if __name__ == '__main__':
    sample_text = "Example String"
    length_of_text = TextAnalyzer.compute_length(sample_text)
    print(length_of_text)