import unicodedata

class UnicodeWordChecker:
    def __init__(self):
        self.target_word = 'critical'

    def normalize_and_check(self, text):
        normalized_text = unicodedata.normalize('NFC', text)
        return self.target_word in normalized_text

if __name__ == '__main__':
    checker = UnicodeWordChecker()
    
    sample_string_1 = "This is a normal line.\nAnother line without the word.\nThis line is critical and important."
    sample_string_2 = "No critical words here. Just some text."
    sample_string_3 = "critical error occurred\nanother line"
    sample_string_4 = "\xc3\x89ritical test"

    print(f"Sample 1 result: {checker.normalize_and_check(sample_string_1)}")
    print(f"Sample 2 result: {checker.normalize_and_check(sample_string_2)}")
    print(f"Sample 3 result: {checker.normalize_and_check(sample_string_3)}")
    print(f"Sample 4 result: {checker.normalize_and_check(sample_string_4)}")