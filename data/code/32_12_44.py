class TextAnalyzer:
    def __init__(self, text):
        self.text = text

    def count_characters(self):
        return len(self.text)

if __name__ == '__main__':
    sample_text1 = "Hello, World!"
    sample_text2 = "Python Programming"
    sample_text3 = ""
    sample_text4 = "OpenAI"
    sample_text5 = "1234567890"

    analyzer1 = TextAnalyzer(sample_text1)
    analyzer2 = TextAnalyzer(sample_text2)
    analyzer3 = TextAnalyzer(sample_text3)
    analyzer4 = TextAnalyzer(sample_text4)
    analyzer5 = TextAnalyzer(sample_text5)

    print(analyzer1.count_characters())
    print(analyzer2.count_characters())
    print(analyzer3.count_characters())
    print(analyzer4.count_characters())
    print(analyzer5.count_characters())