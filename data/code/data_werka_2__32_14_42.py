class PhraseAnalyzer:
    def __init__(self, phrase):
        self.phrase = phrase

    def get_length(self):
        return len(self.phrase)

if __name__ == '__main__':
    sample_phrase = "Hello, World!"
    analyzer = PhraseAnalyzer(sample_phrase)
    print(analyzer.get_length())