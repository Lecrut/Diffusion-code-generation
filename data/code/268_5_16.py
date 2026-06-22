class TextProcessor:
    @staticmethod
    def find_first_word(text):
        if not text or text.isspace():
            return ""
        
        start = 0
        while start < len(text) and text[start] == " ":
            start += 1
        
        end = start
        while end < len(text) and text[end] != " ":
            end += 1
        
        return text[start:end]

if __name__ == '__main__':
    test_cases = [
        ("", ""),
        ("   ", ""),
        ("hello world", "hello"),
        ("  leading space", "leading"),
        ("trailing space ", "trailing"),
        ("singleword", "singleword")
    ]

    for text, expected in test_cases:
        result = TextProcessor.find_first_word(text)
        print(f"Input: '{text}' | Expected: '{expected}' | Result: '{result}'")