class InputCleaner:
    def clean(self, text):
        if not isinstance(text, str):
            raise TypeError("Input must be a string")
        return text.strip()

if __name__ == '__main__':
    cleaner = InputCleaner()
    sample_input = "   Hello World   "
    cleaned_value = cleaner.clean(sample_input)
    print(cleaned_value)