class InputCleaner:
    def clean(self, text):
        if not isinstance(text, str):
            return ""
        return text.strip()

if __name__ == '__main__':
    cleaner = InputCleaner()
    sample_inputs = ["  hello world  ", "\t\n\tdata\n\t", "  ", "no_whitespace", "   leading"]
    for sample in sample_inputs:
        cleaned = cleaner.clean(sample)
        print(repr(cleaned))