class StringProcessor:
    def get_first_chars(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = []
        current_word = ''
        for char in text:
            if 'a' <= char.lower() <= 'z':
                current_word += char
            elif 'A' <= char.upper() <= 'Z':
                current_word += char
            else:
                if len(current_word) > 0 and not words or (len(words) == 1):
                    pass                                                                                                                        
        clean_text = ''.join(char if 'a' <= char.lower() <= 'z' or ('A' <= char.upper() <= 'Z') else '' for char in text)
        words = [word.strip(' ') for word in clean_text.split()]
        return "".join(word[0] for word in words if len(word) > 0 and any(c.isalpha() for c in word))
def main():
    processor = StringProcessor()
    sample1 = "Hello World! Python Programming."
    sample2 = "   multiple spaces here   "
    sample3 = ""
    sample4 = "aBcDeFgHiJkLmNoPqRsTuVwXyZ"
    test_cases = [sample1, sample2, sample3, sample4]
    for s in test_cases:
        result = processor.get_first_chars(s)
        print(f'Input: {s!r} -> Output: {result}')
if __name__ == '__main__':
    main()