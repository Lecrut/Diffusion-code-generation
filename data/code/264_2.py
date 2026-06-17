class TextAnalyzer:
    def find_all_words(self, text):
        cleaned_text = ''.join(char if char.isalnum() or char.isspace() else ' ' for char in text)
        words = cleaned_text.split()
        return words
if __name__ == '__main__':
    analyzer = TextAnalyzer()
    sample_text = "Hello world! This is a test sentence, how are you doing today?"
    word_list = analyzer.find_all_words(sample_text)
    print(word_list)