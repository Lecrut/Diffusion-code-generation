class TextAnalyzer:
    def find_all_words(self, text):
        cleaned_text = ""
        for char in text:
            if 'a' <= char <= 'z' or 'A' <= char <= 'Z' or '0' <= char <= '9':
                cleaned_text += char
        return cleaned_text.split()
if __name__ == '__main__':
    analyzer = TextAnalyzer()
    sample_text = "Hello world! This is a test, how are you doing today?"
    words = analyzer.find_all_words(sample_text)
    print(words)