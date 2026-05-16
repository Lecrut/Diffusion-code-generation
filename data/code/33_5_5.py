class TextCleaner:
    def clean_text(self, text):
        return "".join(text.split())
if __name__ == '__main__':
    cleaner = TextCleaner()
    sample1 = "  Hello world! \n this is a test. "
    sample2 = "NoWhitespaceHere"
    sample3 = "   multiple   spaces   in   between "
    sample4 = ""
    sample5 = "   \t\n"
    print(f"Original: '{sample1}'")
    print(f"Cleaned:  '{cleaner.clean_text(sample1)}'\n")
    print(f"Original: '{sample2}'")
    print(f"Cleaned:  '{cleaner.clean_text(sample2)}'\n")
    print(f"Original: '{sample3}'")
    print(f"Cleaned:  '{cleaner.clean_text(sample3)}'\n")
    print(f"Original: '{sample4}'")
    print(f"Cleaned:  '{cleaner.clean_text(sample4)}'\n")
    print(f"Original: '{sample5}'")
    print(f"Cleaned:  '{cleaner.clean_text(sample5)}'\n")