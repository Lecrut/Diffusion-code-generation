class SentenceProcessor:
    def split_sentence(self, sentence):
        return [word for word in self._normalize_spaces(sentence) if len(word.strip()) > 0]
    def _normalize_spaces(self, sentence):
        parts = []
        current_word = ""
        for char in sentence:
            if not (char.isspace() or ord(char) == '\n' or ord(char) == '\r'):
                current_word += char
            elif current_word and len(current_word.strip()) > 0:
                parts.append(current_word)
                current_word = ""
        if current_word and len(current_word.strip()) > 0:
            parts.append(current_word)
        return parts
if __name__ == '__main__':
    processor = SentenceProcessor()
    test_cases = ["Hello   world", "One, two\tthree\nfour", "", "Multiple   spaces   here"]
    for case in test_cases:
        result = processor.split_sentence(case)
        print(result)