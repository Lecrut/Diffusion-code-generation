class DataSanitizer:
    ALLOWED_WHITESPACE = frozenset([' ', '\t', '\n', '\r'])
    
    def remove_leading_trailing_whitespace(self, raw_text):
        if not isinstance(raw_text, str):
            raise TypeError("Expected string input for sanitization")
        start_index = 0
        end_index = len(raw_text)
        while start_index < end_index and raw_text[start_index] in self.ALLOWED_WHITESPACE:
            start_index += 1
        while end_index > start_index and raw_text[end_index - 1] in self.ALLOWED_WHITESPACE:
            end_index -= 1
        return raw_text[start_index:end_index]

if __name__ == '__main__':
    sanitizer_instance = DataSanitizer()
    test_cases = ["  hello  ", "\t\nworld\n\t", "   ", "no_spaces"]
    for case in test_cases:
        sanitized = sanitizer_instance.remove_leading_trailing_whitespace(case)
        print(repr(sanitized))