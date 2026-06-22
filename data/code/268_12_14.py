class WordExtractor:
    @staticmethod
    def first_word(text):
        words = text.split()
        if words:
            return words[0]
        return ""

if __name__ == '__main__':
    sample_text1 = "  Leading spaces should be ignored. "
    sample_text2 = "Trailing spaces also   should not matter. "
    sample_text3 = " SingleWordNoSpaces "
    empty_string = ""
    
    print(WordExtractor.first_word(sample_text1))
    print(WordExtractor.first_word(sample_text2))
    print(WordExtractor.first_word(sample_text3))
    print(WordExtractor.first_word(empty_string))