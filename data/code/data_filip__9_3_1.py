class InputCleaner:
    def clean(self, text):
        if not isinstance(text, str):
            raise TypeError("Input must be a string")
        return text.strip()

if __name__ == '__main__':
    cleaner = InputCleaner()
    sample_inputs = ["  hello world  ", "\t\n\tdata\n\t", "   ", "no_space"]
    for s in sample_inputs:
        print(repr(cleaner.clean(s)))