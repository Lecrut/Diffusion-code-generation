class StringCleaner:
    def clean(self, text):
        return text.replace(" ", "")

if __name__ == '__main__':
    cleaner = StringCleaner()
    sample_text = "  Hello World! This is a test.  "
    cleaned_text = cleaner.clean(sample_text)
    print(cleaned_text)