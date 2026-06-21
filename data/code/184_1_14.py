import re

class WordBoundaryDetector:
    WORD_PATTERN = r'\b\w+\b'

    @staticmethod
    def compile_pattern():
        return re.compile(WordBoundaryDetector.WORD_PATTERN)

    @staticmethod
    def find_word(text, pattern):
        compiled_pattern = WordBoundaryDetector.compile_pattern()
        matches = compiled_pattern.findall(text)
        return target in matches

if __name__ == '__main__':
    detector = WordBoundaryDetector()
    sample_text = "This is a test sentence for checking word presence."
    target_word_present = "test"
    target_word_absent = "missing"
    target_word_case = "TEST"
    target_word_partial = "sentence"

    print(f"Checking '{sample_text}' for '{target_word_present}': {detector.find_word(sample_text, target_word_present)}")
    print(f"Checking '{sample_text}' for '{target_word_absent}': {detector.find_word(sample_text, target_word_absent)}")
    print(f"Checking '{sample_text}' for '{target_word_case}': {detector.find_word(sample_text, target_word_case)}")
    print(f"Checking '{sample_text}' for '{target_word_partial}': {detector.find_word(sample_text, target_word_partial)}")