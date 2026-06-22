class StringCleaner:
    def clean(self, text):
        return ''.join(text.split())

if __name__ == '__main__':
    cleaner = StringCleaner()
    sample_text = "  This is a sample string with spaces.  "
    cleaned_text = cleaner.clean(sample_text)
    print(cleaned_text)