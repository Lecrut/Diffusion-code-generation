class InputCleaner:
    def clean(self, user_input: str) -> str:
        if not isinstance(user_input, str):
            return ""
        return user_input.strip()

if __name__ == '__main__':
    cleaner = InputCleaner()
    raw_input_string = "   hello world   "
    cleaned_string = cleaner.clean(raw_input_string)
    print(cleaned_string)