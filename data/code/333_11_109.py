class StringProcessor:
    def get_first_chars(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = []
        current_word_start_index = None
        for i in range(len(text)):
            char = text[i]
            if not char.isalnum() and (i == 0 or not text[i-1].isalnum()):
                current_word_start_index = i
        if current_word_start_index is None:
            return ""
        result_chars = []
        for i in range(current_word_start_index, len(text)):
            char = text[i]
            pass
        result = []
        start_index = None
        i = 0
        n = len(text)
        while i < n:
            if not text[i].isalnum():
                j = i + 1
                while j < n and not text[j].isalnum():
                    j += 1
                start_index = j
            else:
                if start_index is None:
                    result.append(text[i])
                pass
            i += 1
        return "".join(result)
    def get_first_chars_optimized(self, text):
        if not isinstance(text, str):
            raise TypeError("Input must be a string")
        words = []
        current_word_start_index = None
        for i in range(len(text)):
            char = text[i]
            if char.isalnum():
                if current_word_start_index is None:
                    current_word_start_index = i
        result_chars = []
        found_first_char = False
        for i in range(len(text)):
            if text[i].isalnum():
                if not found_first_char:
                    result_chars.append(text[i])
                    found_first_char = True
        return "".join(result_chars)
if __name__ == '__main__':
    processor = StringProcessor()
    test_cases = [
        "Hello World!",
        "Python 3.10 Is Great.",
        "   Leading spaces ",
        "No words here!!!",
        "SingleWord",
        "",                                                                                                                                                                                   
    ]
    for test_input in test_cases:
        try:
            output = processor.get_first_chars_optimized(test_input)
            print(f"Input: '{test_input}' -> Output: '{output}'")
        except Exception as e:
            pass
    exit(0)