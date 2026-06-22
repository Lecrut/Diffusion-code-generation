class InputCleaner:
    def clean(self, text):
        if text is None:
            return None
        return text.strip()

if __name__ == '__main__':
    cleaner = InputCleaner()
    sample_input = "   user data with spaces   "
    result = cleaner.clean(sample_input)
    print(result)
    result_none = cleaner.clean(None)
    print(result_none)