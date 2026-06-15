class StringProcessor:
    @staticmethod
    def extract_and_strip_first_word(text: str) -> str:
        parts = text.split()
        if parts:
            return parts[0].strip()
        return ""
if __name__ == '__main__':
    sample1 = "  Hello world! "
    sample2 = "\t  Another test here\n"
    sample3 = "   \t"
    sample4 = "singleword"
    sample5 = ""
    print(f"'{sample1}' -> '{StringProcessor.extract_and_strip_first_word(sample1)}'")
    print(f"'{sample2}' -> '{StringProcessor.extract_and_strip_first_word(sample2)}'")
    print(f"'{sample3}' -> '{StringProcessor.extract_and_strip_first_word(sample3)}'")
    print(f"'{sample4}' -> '{StringProcessor.extract_and_strip_first_word(sample4)}'")
    print(f"'{sample5}' -> '{StringProcessor.extract_and_strip_first_word(sample5)}'")