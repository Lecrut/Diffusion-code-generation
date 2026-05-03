class TextCleaner:
    def clean_text(self, text):
        return "".join(text.split())
if __name__ == '__main__':
    cleaner = TextCleaner()
    sample_text1 = "  Hello world! \n  This is a test. "
    sample_text2 = "NoWhitespaceHere"
    sample_text3 = "   Multiple    spaces   and    newlines\t"
    result1 = cleaner.clean_text(sample_text1)
    result2 = cleaner.clean_text(sample_text2)
    result3 = cleaner.clean_text(sample_text3)
    print(f"Original 1: '{sample_text1}'")
    print(f"Cleaned 1: '{result1}'")
    print("-" * 20)
    print(f"Original 2: '{sample_text2}'")
    print(f"Cleaned 2: '{result2}'")
    print("-" * 20)
    print(f"Original 3: '{sample_text3}'")
    print(f"Cleaned 3: '{result3}'")