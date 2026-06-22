class InputCleaner:
    def clean(self, text):
        if text is None:
            return ""
        return text.strip()

if __name__ == "__main__":
    cleaner = InputCleaner()
    sample_inputs = ["  Hello World  ", "\tPython\n", "   ", "NoSpace"]
    for s in sample_inputs:
        result = cleaner.clean(s)
        print(f"Cleaned: [{result}]")