class WordExtractor:
    def extract_first_word(self, text: str) -> str:
        if not text:
            return ""
        first_word = ""
        for char in text:
            if 'a' <= char <= 'z' or 'A' <= char <= 'Z' or char.isspace():
                if first_word == "":
                    first_word += char
                else:
                    break
            elif first_word != "":
                break
            elif not first_word and char.isalnum():
                 first_word += char
        words = text.split()
        if words:
            return words[0]
        else:
            return ""
if __name__ == '__main__':
    extractor = WordExtractor()
    sample1 = "Hello world, this is a test."
    sample2 = "   leading spaces matter."
    sample3 = "singleword"
    sample4 = ""
    sample5 = "  \t\n"
    print(f"Input: '{sample1}' -> Output: '{extractor.extract_first_word(sample1)}'")
    print(f"Input: '{sample2}' -> Output: '{extractor.extract_first_word(sample2)}'")
    print(f"Input: '{sample3}' -> Output: '{extractor.extract_first_word(sample3)}'")
    print(f"Input: '{sample4}' -> Output: '{extractor.extract_first_word(sample4)}'")
    print(f"Input: '{sample5}' -> Output: '{extractor.extract_first_word(sample5)}'")