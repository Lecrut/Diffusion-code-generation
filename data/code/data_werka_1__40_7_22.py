class TextAnalyzer:

    def __init__(self):
        self.alphabet = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

    def find_first_word_initials(self, text: str) -> list:
        words = text.split()
        initials = []
        for word in words:
            if any((char in self.alphabet for char in word)):
                initials.append(word[0])
        return initials
if __name__ == '__main__':
    analyzer = TextAnalyzer()
    sample_text_1 = 'Hello world! This is a test.'
    sample_text_2 = '   Leading spaces and punctuation!!!'
    sample_text_3 = '123numbers only'
    sample_text_4 = '!@#$%^&*() no words here'
    print(analyzer.find_first_word_initials(sample_text_1))
    print(analyzer.find_first_word_initials(sample_text_2))
    print(analyzer.find_first_word_initials(sample_text_3))
    print(analyzer.find_first_word_initials(sample_text_4))