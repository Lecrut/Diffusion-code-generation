class StringCleaner:
    def clean(self, text: str) -> str:
        if not isinstance(text, str):
            raise TypeError("Input must be a string")
        return text.strip()

if __name__ == '__main__':
    cleaner = StringCleaner()
    sample_input = "  hello world  "
    result = cleaner.clean(sample_input)
    print(result)