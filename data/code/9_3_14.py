class StringCleaner:
    def clean_input(self, text):
        if not isinstance(text, str):
            raise TypeError("Input must be a string")
        return text.strip()

if __name__ == '__main__':
    cleaner = StringCleaner()
    result = cleaner.clean_input("  hello world  ")
    print(repr(result))