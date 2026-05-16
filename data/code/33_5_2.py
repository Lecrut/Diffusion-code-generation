class TextCleaner:
    def clean_text(self, text):
        return "".join(text.split())
if __name__ == '__main__':
    cleaner = TextCleaner()
    sample1 = "  Hello World! \n This is a test. "
    sample2 = "NoWhitespaceHere"
    sample3 = "   \t\nMultiple   spaces   and\ttabs "
    sample4 = ""
    result1 = cleaner.clean_text(sample1)
    result2 = cleaner.clean_text(sample2)
    result3 = cleaner.clean_text(sample3)
    result4 = cleaner.clean_text(sample4)
    print(f"Original 1: '{sample1}'")
    print(f"Cleaned 1: '{result1}'")
    print("-" * 20)
    print(f"Original 2: '{sample2}'")
    print(f"Cleaned 2: '{result2}'")
    print("-" * 20)
    print(f"Original 3: '{sample3}'")
    print(f"Cleaned 3: '{result3}'")
    print("-" * 20)
    print(f"Original 4: '{sample4}'")
    print(f"Cleaned 4: '{result4}'")