import unicodedata

class WordChecker:
    WORD_TO_CHECK = 'critical'

    @staticmethod
    def normalize_to_nfc(text):
        return unicodedata.normalize('NFC', text)

    @classmethod
    def check_word_presence(cls, multi_line_string):
        normalized_text = cls.normalize_to_nfc(multi_line_string)
        return cls.WORD_TO_CHECK in normalized_text

if __name__ == '__main__':
    sample_string_1 = "This is a normal line.\nAnother line without the word.\nThis line is critical and important."
    sample_string_2 = "No critical words here. Just some text."
    sample_string_3 = "critical error occurred\nanother line"
    sample_string_4 = "\xc3\x89ritical test"

    checker = WordChecker()
    print(f"Sample 1 result: {checker.check_word_presence(sample_string_1)}")
    print(f"Sample 2 result: {checker.check_word_presence(sample_string_2)}")
    print(f"Sample 3 result: {checker.check_word_presence(sample_string_3)}")
    print(f"Sample 4 result: {checker.check_word_presence(sample_string_4)}")