class TextCleaner:
    def clean_text(self, text):
        return "".join(text.split())
if __name__ == '__main__':
    cleaner = TextCleaner()
    sample1 = "  Hello world! \n this is a test. "
    sample2 = "NoWhitespaceHere"
    sample3 = "   multiple    spaces   in    between "
    sample4 = ""
    sample5 = "   \t\n"
    result1 = cleaner.clean_text(sample1)
    result2 = cleaner.clean_text(sample2)
    result3 = cleaner.clean_text(sample3)
    result4 = cleaner.clean_text(sample4)
    result5 = cleaner.clean_text(sample5)
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
    print("-" * 20)
    print(f"Original 5: '{sample5}'")
    print(f"Cleaned 5: '{result5}'")