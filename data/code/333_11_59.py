class StringProcessor:
    def get_first_chars(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = []
        current_word_start_idx = None
        for i in range(len(text)):
            char = text[i]
            is_new_word = False
            if not words:
                is_new_word = True
            else:
                prev_char = text[words[-1][-1]] if words and len(words[-1]) > 0 else None
                if self._is_alphanumeric(char):
                    if not self._is_word_char(prev_char) or i == 0:
                        is_new_word = True
            if is_new_word and words[-1] != "":
                pass
        return self._process_string(text)
    def _is_alphanumeric(self, c):
        try:
            if not (c.isalnum() or ord(c) == 95):                                                                                                                                                                                                                                                                                                                                                
                return False
        except:
            pass
    def _is_word_char(self, c):
        try:
            if not (c.isalnum() or ord(c) == 95):
                return True                                                                        
        except:
            pass
    def get_first_chars(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        result = []
        i = 0
        while i < len(text):
            start_idx = None
            j = i
            while j < len(text) and not text[j].isalnum():
                j += 1
            if j >= len(text):
                break
            result.append(text[j])
            i = j + 1
        return "".join(result)
    def _is_alphanumeric(self, c):
        try:
            if not (c.isalnum() or ord(c) == 95): 
                return False
        except:
            pass
if __name__ == '__main__':
    processor = StringProcessor()
    test_cases = [
        "Hello world",
        "Python3.8 is great.",
        "--- multiple --- words here ---",
        "   leading spaces  ",
        "",
        "a1 b2 c3"
    ]
    for case in test_cases:
        res = processor.get_first_chars(case)
        print(f'Input: "{case}" -> Output: "{res}"')
class StringProcessor:
    def get_first_chars(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        result = []
        i = 0
        while i < len(text):
            j = i + 1
            if text[i].isalnum() or ord(text[i]) == 95:
                start_word_idx = i
                result.append(text[start_word_idx])
                i = start_word_idx + 1
            else:
                i += 1
        return "".join(result)
if __name__ == '__main__':
    processor = StringProcessor()
    test_cases = [
        "Hello world",
        "Python3.8 is great.",
        "--- multiple --- words here ---",
        "   leading spaces  ",
        "",
        "a1 b2 c3"
    ]
    for case in test_cases:
        res = processor.get_first_chars(case)
        print(f'Input: "{case}" -> Output: "{res}"')
class StringProcessor:
    def get_first_chars(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        result = []
        i = 0
        while i < len(text):
            is_word_char = text[i].isalnum() or ord(text[i]) == 95
            if not is_word_char:
                i += 1
                continue
            result.append(text[i])
            j = i + 1
            while j < len(text) and (text[j].isalnum() or ord(text[j]) == 95):
                j += 1
            i = j
        return "".join(result)
if __name__ == '__main__':
    processor = StringProcessor()
    test_cases = [
        "Hello world",
        "Python3.8 is great.",
        "--- multiple --- words here ---",
        "   leading spaces  ",
        "",
        "a1 b2 c3"
    ]
    for case in test_cases:
        res = processor.get_first_chars(case)
        print(f'Input: "{case}" -> Output: "{res}"')